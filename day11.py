def calculate_adjacent(data):
    '''returns a matrix the same size as the input, where each entry corresponds to how many 
    adjacent entries in input are occupied
    '''
    store = np.zeros(data.shape, dtype=int)

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            center = i,j
            if data[center]==0:
                continue

            # calculates number of adjacent seats
            subset = np.copy(data)
            subset[center] = 0
            subset = subset[max(center[0]-1,0):min(data.shape[0], center[0]+2), max(0,center[1]-1):min(data.shape[1], center[1]+2)]

            store[center] = (subset==1).sum()
    return store
	
def calculate_in_view(data):
    '''returns a matrix the same size as the input, where each entry corresponds to how many 
    entries "in view" of the current location are occupied
    '''
    store = np.zeros(data.shape, dtype=int)
    
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            center = i,j
            if data[center]==0:
                continue
                
            num_in_view = 0
            
            # look down
            # look right
            # look left
            # look up
            # look down-right
            # look down-left
            # look up-right
            # look up-left
            for look in [data[min(center[0]+1, data.shape[0]):, center[1]], data[center[0], min(center[1]+1, data.shape[1]):], 
                         data[center[0], 0:center[1]][::-1], data[0:center[0], center[1]][::-1], 
                         np.diag(data[min(center[0]+1, data.shape[0]):, min(center[1]+1, data.shape[1]):]),
                         np.diag(np.fliplr(data[min(center[0]+1, data.shape[0]):, 0:center[1]])),
                         np.diag(data[0:min(center[0], data.shape[0]), min(center[1]+1, data.shape[1]):][::-1]),
                         np.diag(np.fliplr(data[0:min(center[0], data.shape[0]), 0:min(center[1], data.shape[1])][::-1]))]:
                try:
                    num_in_view += look[look!=0][0]==1
                except IndexError:
                    pass
            store[center] = num_in_view
    return store
	
def part_1(dt):
    data = np.copy(dt)
    while True:
        adjacent = calculate_adjacent(data)

        # occupied seat with 4 adjacent people will leave
        leavers = (data==1)&(adjacent>=4)
        # empty seats with nobody next to them will become occupied
        arrivers = (data==-1)&(adjacent==0)

        if leavers.sum()==0 and arrivers.sum()==0:
			# indicates nobody moved
            break

        data[leavers] = -1
        data[arrivers] = 1

    return (data==1).sum()
	
def part_2(dt):
    data = np.copy(dt)
    while True:
        in_view = calculate_in_view(data)

        # occupied seat with 5 adjacent people will leave
        leavers = (data==1)&(in_view>=5)
        # empty seats with nobody next to them will become occupied
        arrivers = (data==-1)&(in_view==0)

        if leavers.sum()==0 and arrivers.sum()==0:
			# indicates nobody moved
            break

        data[leavers] = -1
        data[arrivers] = 1

    return (data==1).sum()
	
def main():
    with open('day11.txt', 'r') as f:
        txt = f.read().strip()
    f.close()

    # -1 indicates open seat
    # 1 will indicate filled seat
    # 0 indicates floor

    data = -1*(np.array([list(x) for x in txt.split()])=='L').astype(int)
    
    # part 1
    print(part_1(data))

    # part 1
    print(part_2(data))
	
if __name__=='__main__':
	import numpy as np
	main()