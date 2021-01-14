def part_1(directions):
    status = {} # store whether each node is face up or face down
    # black is True
    # white is False

    for direction in directions:
        # walk a single path, adding nodes as necessary
        current_location = origin

        while len(direction)>0:
            for step, (x,y) in guide.items():
                if direction.startswith(step):
                    direction = direction[len(step):]
                    new_location = (current_location[0]+x, current_location[1]+y)
                    if new_location not in status:
                        status[new_location] = False
                    
                    current_location = new_location
                    
        # now reached the last location on this path
        # flip the tile
        status[current_location] = not status[current_location]
        
    return status
    
def part_2(orig_status):
    status = orig_status.copy()
    
    for i in range(100):
        # pad edges first
        to_check = list(status.items())
        for origin,flipped in to_check:
            if flipped:
                # any tile adjacent to a black tile may need to be flipped to black!
                for neighbor in guide.values():
                    if (origin[0]+neighbor[0], origin[1]+neighbor[1]) not in status:
                        status[origin[0]+neighbor[0], origin[1]+neighbor[1]] = False

        # flip tiles
        adjacent = [False] * 6
        to_check = list(status.items())
        next_status = status.copy()

        for origin, flipped in to_check:
            for i,neighbor in enumerate(guide.values()):
                try:
                    adjacent[i] = status[origin[0]+neighbor[0], origin[1]+neighbor[1]]
                except KeyError:
                    status[origin[0]+neighbor[0], origin[1]+neighbor[1]] = False
                    adjacent[i] = False

            num_adjacent = sum(adjacent)

            # black with zero or more than 2 black
            if flipped:
                if num_adjacent==0 or num_adjacent>2:
                    #print('Flipping {} to white'.format(origin))
                    next_status[origin] = False

            # white with 2 black
            elif not flipped:
                if num_adjacent==2:
                    #print('Flipping {} to black'.format(origin))
                    next_status[origin] = True

        status = next_status
    return status
        
def main():
    with open('day24.txt', 'r') as f:
        txt = f.read().strip()
    f.close()
   
    # part 1
    status = part_1(txt.split())
    print(sum(list(status.values())))
    
    # part 2
    final_status = part_2(status)
    print(sum(list(final_status.values())))
    
if __name__=='__main__':
    guide = {'e':(1, 0), 
        'se':(0.5, -0.5), 
        'sw':(-0.5, -0.5), 
        'w':(-1, 0), 
        'nw':(-0.5, 0.5), 
        'ne':(0.5, 0.5)}

    origin = (0,0)
    
    main()