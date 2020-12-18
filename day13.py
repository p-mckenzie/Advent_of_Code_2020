def part_1(IDs, departure_time):
    from math import ceil
    min_ID = 0
    min_wait = IDs[0]

    for ID in IDs:
        if ID=='x':
            continue
        wait_time = ceil(departure_time/ID)*ID - departure_time
        if wait_time<min_wait:
            min_wait = wait_time
            min_ID = ID
            
    return min_ID*min_wait
   
def part_2(IDs):
    # store (divisor, remainder) pairs
    B = [(int(IDs[k]), k) for k in range(len(IDs)) if IDs[k] != 'x']

    lcm = 1
    time = 0
    for i in range(len(B)-1):
        # update least common multiple for all busses including bus i
        lcm *= B[i][0]
        
        # find interval and remainder for next bus
        bus_id = B[i+1][0]
        idx = B[i+1][1]
        
        # while next bus doesn't arrive at appropriate time, increment time by lcm
        # aka proceed to next time increment where every previous bus arrives appropriately 
        ## until we find a time where this bus also arrives appropriately
        while (time + idx) % bus_id != 0:
            time += lcm

    return time
   
def main():
    with open('day13.txt', 'r') as f:
        txt = f.read().strip()
    f.close()

    departure_time, IDs = txt.split()

    departure_time = int(departure_time)
    IDs = [int(ID) if ID!='x' else ID for ID in IDs.split(',')]
    
    print(part_1(IDs, departure_time))
    print(part_2(IDs))
    
if __name__=='__main__':
    main()