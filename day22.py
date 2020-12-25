def play_regular(input_decks):
    '''Regular game for part 1 - highest card wins'''
    decks = input_decks.copy()
    while len(decks[0])>0 and len(decks[1])>0:
        # draw cards
        player_1 = decks[0][0]
        player_2 = decks[1][0]            
        decks[0] = decks[0][1:]
        decks[1] = decks[1][1:]

        if player_1>player_2:
            decks[0].append(player_1)
            decks[0].append(player_2)
            
        elif player_1<player_2:
            decks[1].append(player_2)
            decks[1].append(player_1)

        else:
            break
        
    # return the winning deck
    return sorted(decks, key=lambda x:-len(x))[0]
    
def convert(inp):
    # hashes input deck to string
    return 'p1'+''.join([str(x) for x in inp[0]])+'p2'+''.join([str(x) for x in inp[1]])
    
def play_recursive(input_decks, depth=0):
    '''Recursive game for part 2 - highest card wins IF there are enough cards remaining, otherwise play
    a sub-game with smaller deck based on the cards drawn.'''
    rounds = set() # new memory for each game
    decks = input_decks.copy()
    round = 1
    while len(decks[0])>0 and len(decks[1])>0:
        converted = convert(decks)

        # check if layout has been played before THIS GAME
        if converted in rounds:
            if depth>0:
                return decks
            else:
                return sorted(decks, key=lambda x:-len(x))[0]
        else:
            rounds.add(converted)
           
        # draw cards!
        player_1 = decks[0][0]
        player_2 = decks[1][0]            
        decks[0] = decks[0][1:]
        decks[1] = decks[1][1:]
        
        if len(decks[0])>=player_1 and len(decks[1])>=player_2:
            # enough to recurse!
            result = play_recursive([decks[0][:player_1], decks[1][:player_2]], depth=depth+1)
            if result:
                # player 1 won the sub-game
                decks[0].append(player_1)
                decks[0].append(player_2)
            else:
                decks[1].append(player_2)
                decks[1].append(player_1)
        
        else:
            # winner is player with larger card
            if player_1>player_2:
                decks[0].append(player_1)
                decks[0].append(player_2)
            elif player_1<player_2:
                decks[1].append(player_2)
                decks[1].append(player_1)
                
            else:
                break
        round += 1
        
    if depth>0:
        # sub-game, so all that matters is whether the game is done
        return len(decks[0])!=0
    else:
        # overall game - return the winning deck
        return sorted(decks, key=lambda x:-len(x))[0]
        
def main():
    with open('day22.txt', 'r') as f:
        txt = f.read().strip()
    f.close()

    from re import findall

    decks = [[int(y) for y in findall('\d+', x.split(':')[1])] for x in txt.split('\n\n')]

    # part 1
    winning_deck = play_regular(decks)
    print(sum([winning_deck[i]*(len(winning_deck)-i) for i in range(len(winning_deck))]))

    # part 2
    winning_deck = play_recursive(decks)
    print(sum([winning_deck[i]*(len(winning_deck)-i) for i in range(len(winning_deck))]))
    
if __name__=='__main__':
    main()