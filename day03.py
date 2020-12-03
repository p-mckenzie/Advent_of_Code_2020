def count_trees(x_slope, y_slope, data):

    row, col = 0,0
    tree_count = 0

    while row<len(data):
        spot = data[row][col]
        if spot=='#':
            tree_count += 1

        row, col = row+y_slope, col+x_slope
        # update column using modulo so we don't run off the page
        col = col % len(data[0])
        
    return tree_count
	
def main():
    # read data and store each row as a string, in a list
    with open('day03.txt', 'r') as f:
        txt = f.read().strip()
    f.close()
    data  = txt.split('\n')
    
    # part 1
    print(count_trees(3,1, data))
    
    # part 2
    from functools import reduce

    counts = [count_trees(x_sl,y_sl, data) for x_sl, y_sl in [(1,1), (3,1), (5,1), (7,1), (1,2)]]
    print(reduce(lambda x, y: x * y, counts, 1))
	
if __name__=='__main__':
	main()