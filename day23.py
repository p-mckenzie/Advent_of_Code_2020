def format_order(ordr, start):
    '''Accepts a dictionary of key:next_key pairs, returns them in order from start'''
    output = ''
    
    current = start
    for i in range(len(ordr)):
        output += str(current)
        current = ordr[current]
    return output
    
def reformatted(txt, n, vocal=False):
    '''implementing a linked list with a dictionary. 
    Each key is a cup number, and the corresponding value is the next cup. 
    Moving cups is just a matter of relinking them'''
    
    order = {}
    start = txt[0]
    for i in range(-1,len(txt)-1):
        order[txt[i]] = txt[i+1]

    max_cup = max(txt)

    for move in range(n):
        if vocal and move%(n//50+1)==0:
            print("Move #{}, {}% done".format(move, round(100*(move/n), 2)))

        # take out 3 cups
        removed_1 = order[start]
        removed_2 = order[removed_1]
        removed_3 = order[removed_2]
        after_removed  = order[removed_3]
        taken_out = [removed_1, removed_2, removed_3]

        # find destination cup
        search_cup = start-1
        while True:
            if search_cup<=0:
                search_cup = max_cup
            #print("Searching:", search_cup)
            if search_cup not in taken_out:
                destination_cup = search_cup
                break
            search_cup -= 1
            
        # ------------- only need to update 3 locations! ----------------------

        # connect "hole" where taken out cups are being removed
        order[start] = after_removed

        # connect last taken out cup to the next after destination cup
        order[removed_3] = order[destination_cup]

        # connect destination cup to 1st taken out
        order[destination_cup] = removed_1

        start = after_removed
        
    return order
        
def main():
    txt = '614752839'

    # part 1
    print(format_order(reformatted([int(x) for x in txt], n=100), 1)[1:])
    
    # part 2
    result = reformatted([int(x) for x in txt]+list(range(int(max(txt))+1,1000000+1)), 
                n=10000000)
    print(result[1]*result[result[1]])
    
if __name__=='__main__':
    main()