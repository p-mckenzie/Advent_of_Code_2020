def find_combo(data, n):
    '''Iterates through combinations of size n for the elements in data, returns the product of
    the first combination thats elements sum to 2020'''
    from itertools import combinations
    for pair in combinations(data, n):
        if sum(pair)==2020:
            return np.product(pair)

def main():
    # read data into numpy array
    
    with open('day01.txt') as f:
        txt = f.read().strip()
    f.close()

    data = np.array(txt.split('\n'), dtype=np.int64)
    
    # part 1
    print(find_combo(data, 2))
    
    # part 2
    print(find_combo(data, 3))
    
if __name__=='__main__':
    import numpy as np
    main()