def part_1(txt):
    dim = len(txt.split()[0])
    data = np.zeros((dim,dim,dim), dtype=bool)

    data[1] = np.array([list(x) for x in txt.replace('#', '1').replace('.', '0').split()], dtype=np.int8).astype(bool)

    next_data = np.pad(data, pad_width=1, mode='constant')

    # data[z,y,x]
    for cycle in range(6):
        for z in range(data.shape[0]):
            for y in range(data.shape[1]+1):
                for x in range(data.shape[2]+1):
                    try:
                        root_status = data[z,y,x]
                    except:
                        root_status = False
                    count_active = data[max(0, z-1):z+2, max(0, y-1):y+2, max(0,x-1):x+2].sum()

                    # don't count root as a neighbor
                    if root_status:
                        count_active -= 1

                    if root_status and count_active in [2,3]:
                        continue
                    elif root_status:
                        # becomes inactive
                        next_data[z+1,y+1,x+1] = False
                    elif not root_status and count_active==3:
                        # becomes active
                        next_data[z+1,y+1,x+1] = True

        data = next_data
        next_data = np.pad(data, pad_width=1, mode='constant')
    return data.sum()
    
def part_2(txt):
    dim = len(txt.split()[0])
    data = np.zeros((dim,dim,dim,dim), dtype=bool)

    data[1,1] = np.array([list(x) for x in txt.replace('#', '1').replace('.', '0').split()], dtype=np.int8).astype(bool)

    next_data = np.pad(data, pad_width=1, mode='constant')

    # data[z,y,x]
    for cycle in range(6):
        for w in range(data.shape[0]):
            for z in range(data.shape[1]):
                for y in range(data.shape[2]+1):
                    for x in range(data.shape[3]+1):
                        try:
                            root_status = data[w,z,y,x]
                        except:
                            root_status = False
                        count_active = data[max(0, w-1):w+2, max(0, z-1):z+2, max(0, y-1):y+2, max(0,x-1):x+2].sum()

                        # don't count root as a neighbor
                        if root_status:
                            count_active -= 1

                        if root_status and count_active in [2,3]:
                            continue
                        elif root_status:
                            # becomes inactive
                            next_data[w+1,z+1,y+1,x+1] = False
                        elif not root_status and count_active==3:
                            # becomes active
                            next_data[w+1,z+1,y+1,x+1] = True

        data = next_data
        next_data = np.pad(data, pad_width=1, mode='constant')
    return data.sum()
    
def main():
    with open('day17.txt', 'r') as f:
        txt = f.read().strip()
    f.close()

    print(part_1(txt))
    print(part_2(txt))
    
if __name__=='__main__':
    import numpy as np
    main()