def turn(direction, indicator):
    if indicator=='R':
        # clockwise
        return direction[1], -direction[0]
    else:
        # counter-clockwise
        return -direction[1], direction[0]
        
def part_1(txt):
    location = 0,0 # start at origin
    facing = 1,0 # east

    for instruction in txt.split():
        direction = instruction[0]
        distance = int(instruction[1:])

        if direction=='F':
            # go forward
            location = location[0]+facing[0]*distance, location[1]+facing[1]*distance
        elif direction=='N':
            location = location[0], location[1]+distance
        elif direction=='S':
            location = location[0], location[1]-distance
        elif direction=='E':
            location = location[0]+distance, location[1]
        elif direction=='W':
            location = location[0]-distance, location[1]
        else:
            # turn right or left
            while distance>0:
                facing = turn(facing, direction)
                distance -= 90
    return abs(location[0])+abs(location[1])
    
def part_2(txt):
    location = 0,0 # start at origin
    facing = 1,0 # east
    waypoint = 10,1

    for instruction in txt.split():
        direction = instruction[0]
        distance = int(instruction[1:])

        if direction=='F':
            # go forward
            location = location[0]+waypoint[0]*distance, location[1]+waypoint[1]*distance
        elif direction=='N':
            waypoint = waypoint[0], waypoint[1]+distance
        elif direction=='S':
            waypoint = waypoint[0], waypoint[1]-distance
        elif direction=='E':
            waypoint = waypoint[0]+distance, waypoint[1]
        elif direction=='W':
            waypoint = waypoint[0]-distance, waypoint[1]
        else:
            # turn right or left
            while distance>0:
                waypoint = turn(waypoint, direction)
                distance -= 90
    return abs(location[0])+abs(location[1])

def main():
    with open('day12.txt', 'r') as f:
        txt = f.read().strip()
    f.close()
        
    # part 1
    print(part_1(txt))

    # part 2
    print(part_2(txt))

if __name__=='__main__':
    import numpy as np
    main()