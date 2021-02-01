def segment(tile):
    # segments a square tile into the top, bottom, left, and right edge (returns a string for each)
    top = tile[:10]
    bottom = tile[-10:]
    # top to bottom
    right = tile[9::11]
    left = tile[::11]
    return top, bottom, left, right

def rotate(tile):
    # performs a 90 degree clockwise rotation
    sz = len(tile.split()[0])
    return '\n'.join([''.join([x[i] for x in tile.split()[::-1]]) for i in range(sz)])

def flip(tile):
    # mirror across x axis
    return '\n'.join([x[::-1] for x in tile.split()])
    
def shrink(tile):
    # reduces an nxn square tile to an (n-1)x(n-1) square tile by removing the first and last element
    # of each row & column
    return '\n'.join([x[1:-1] for x in tile.split()[1:-1]])
    
def fit(i, tile_ids, orientations, tiles):
    # recursive function that attempts to fit tiles into a square grid (checking all 8 flip/rotations of each tile,
    # in each position)
    
    # choose a tile for each position on the grid
    for tile_id in tiles:
        if tile_id in tile_ids:
            continue
        for orientation in range(8):
            #print('\t'*i, 'Orientation', orientation, tile_id)
            # spin the tile and check each rotation
            
            fits = True
            if i-int(len(tiles)**.5)>=0:
                # check that bottom of existing tile fits top of new tile
                fits = fits and (tiles[tile_ids[i-int(len(tiles)**.5)]][orientations[i-int(len(tiles)**.5)]][1]==tiles[tile_id][orientation][0])
            if i-1>=0 and i%int(len(tiles)**.5)>0:
                # check that right of existing tile fits left of new tile
                fits = fits and (tiles[tile_ids[i-1]][orientations[i-1]][3]==tiles[tile_id][orientation][2])
            if fits:
                # store information
                tile_ids[i] = tile_id
                orientations[i] = orientation
                
                if i==len(tiles)-1:
                    # the last tile fit, we're done!
                    return True
                
                # check for next tile
                if not fit(i+1, tile_ids, orientations, tiles):
                    # reset information
                    tile_ids[i] = 0
                    orientations[i] = 0
                    #print('\t'*i, 'Orientation', orientation, tile_id)
                    continue
                else:
                    return True
    return False
    
def part_1(txt):
    from collections import defaultdict

    tiles = defaultdict(list) # store each configuration of edges
    master_tiles = defaultdict(list) # store each configuration of whole tiles

    for tile in txt.split('\n\n'):
        tile_id, contents = tile.split(':\n')
        tile_id = int(tile_id.split()[1])
        
        # will be 8 orientation options for each tile:
        # original, rot90, rot180, rot270
        tiles[tile_id].append(segment(contents))
        master_tiles[tile_id].append(contents)
        for i in range(3):
            contents = rotate(contents)
            tiles[tile_id].append(segment(contents))
            master_tiles[tile_id].append(contents)
            
        
        #flipped, flip90, flip180, flip270
        contents = flip(contents)
        tiles[tile_id].append(segment(contents))
        master_tiles[tile_id].append(contents)
        for i in range(3):
            contents = rotate(contents)
            tiles[tile_id].append(segment(contents))
            master_tiles[tile_id].append(contents)
    
    # stores (tile_id, orientation) pairs
    tile_ids = [0]*len(tiles)
    orientations = [0] * len(tiles)

    i = 0
    # run recursive function to arrange tiles and ensure it succeeds
    assert fit(i, tile_ids, orientations, tiles)
    return tiles, master_tiles, tile_ids, orientations
    
def part_2(tiles, master_tiles, tile_ids, orientations):
    '''Builds the final layout based on tile_ids, orientations, then iterates through all 8 
    orientations (4 rotations, 4 flipped rotations) looking for the maximum number of sea monsters. Returns
    "rough waters", the count of # that appear in the final layout with the most sea monsters, but 
    are not part of a sea monster.'''
    # remove (matching) edges of each tile to create the shrunken layout
    shrunken_layout = '\n'.join(['\n'.join([''.join([entry[i] for entry in [shrink(master_tiles[tile_ids[i]][orientations[i]]).split() 
                                                                          for i in range(row*int(len(tiles)**.5), (row+1)*int(len(tiles)**.5))]])
                                          for i in range(8)]) 
                               for row in range(int(len(tiles)**.5))])
                               
    monster = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''
 
    layout = shrunken_layout
    rough_waters = layout.count('#')
    mon_x, mon_y = len(monster.split('\n')), len(monster.split('\n')[0])

    # iterate through 8 orientations (4 rotations of original, 4 rotations of transformed)
    for i in range(8):
        if i==4:
            layout = flip(layout)
        else:
            layout = rotate(layout)
            
        monsters = []
        
        # iterate through slices of the layout, the size of the monster, looking for a match
        for start_row in range(len(layout.split())-mon_x+1):
            for start_col in range(len(layout.split()[0])-mon_y+1):
                
                slce = '\n'.join([x[start_col:start_col+mon_y] for x in layout.split()[start_row:start_row+mon_x]])
                
                if min([slce[i]=='#' for i in range(len(monster)) if monster[i]=='#']):
                    # slice looks like a monster!
                    monsters.append((start_row, start_col))
                    
        # update the # of rough waters, if more monsters are present in this orientation
        if rough_waters>layout.count("#")-monster.count("#")*len(monsters):
            rough_waters = layout.count('#')-monster.count("#")*len(monsters)
        
    return rough_waters
    
def main():
    with open('day20.txt', 'r') as f:
        txt = f.read().strip()
    f.close()
    
    # part 1
    tiles, master_tiles, tile_ids, orientations = part_1(txt)
    print(tile_ids[0]*tile_ids[int(len(tiles)**.5)-1]*tile_ids[-int(len(tiles)**.5)]*tile_ids[-1])
    
    # part 2
    print(part_2(tiles, master_tiles, tile_ids, orientations))
    
if __name__=='__main__':
    main()