def calc_seat_num(x):
    '''converts input text (x) to a seat number, following binary search using l
    to denote lower, u to denote upper'''
    seat_num = range(2**len(x))
    for item in x:
        if item=='u':
            seat_num = seat_num[len(seat_num)//2:]
        elif item=='l':
            seat_num = seat_num[:len(seat_num)//2]
    assert len(seat_num)==1
    return seat_num[0]
    
def find_missing_seat(seats):
    '''Iterate through seat_ids in seats, finding the pair with a missing neighbor.
    That neighbor is the seat we're looking for.'''
    # sort seats ascending by seat_id
    seats.sort()
    missing = []
    for i in range(1,len(seats)-1):
        if seats[i]==seats[i-1]+1 and seats[i]==seats[i+1]-1:
            continue
        else:
            missing.append(seats[i])

    # check that we've found 2 seats with 1 missing in-between        
    assert len(missing)==2
    assert missing[1]-1==missing[0]+1
    
    # return location of missing seat
    return missing[0]+1

def main():
    with open('day05.txt', 'r') as f:
        txt = f.read().strip()
    f.close()

    # iterate through boarding passes, calculate & store seat ids
    data = txt.split()
    seats = []

    for datum in data:
        # replace text so that row, col both use u/l before feeding to calc_seat_num
        row, col = datum[:7].replace('F','l').replace('B','u'), datum[7:].replace('L', 'l').replace('R', 'u')

        seat_id = 8*calc_seat_num(row)+calc_seat_num(col)

        # store location of seat for part 2
        seats.append(seat_id)
        
    # part 1
    print(max(seats))

    # part 2
    print(find_missing_seat(seats))

if __name__=='__main__':
    import numpy as np
    main()