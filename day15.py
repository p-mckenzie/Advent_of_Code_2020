def main():
    txt = '9,19,1,6,0,5,4'

    data = [int(x) for x in txt.split(',')]

    from collections import defaultdict

    for goal in 2020, 30000000:
        store = defaultdict(list)
        for turn in range(1, goal+1):
            if turn<len(data)+1 or spoken not in store:
                # run through input
                spoken = data[turn-1]

            else:
                if len(store[spoken])==1:
                    spoken = 0
                else:
                    spoken = store[spoken][-1]-store[spoken][-2]

            # update counts
            store[spoken].append(turn)
            
            # only need to maintain 2 occurrences of each spoken #
            if len(store[spoken])>2:
                store[spoken] = store[spoken][-2:]

        print(spoken)
        
if __name__=='__main__':
    main()