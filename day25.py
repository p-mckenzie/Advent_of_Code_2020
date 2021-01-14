def handshake(subject_number, public_number, loop_size=20201227):
    # searches through loop_size, looking for the # of loops required to achieve the public_number
    val = 1

    for i in range(1,loop_size):
        val *= subject_number
        val = val % 20201227
        if val==public_number:
            return i
        
def main():
    with open('day25.txt', 'r') as f:
        public_card, public_door = f.read().strip().split()
        public_card = int(public_card)
        public_door = int(public_door)
        
    f.close()

    secret_card = handshake(7, public_card)
    secret_door = handshake(7, public_door)

    # calculate encryption key
    val = 1
    for loop in range(secret_card):
        val *= public_door
        val = val % 20201227
    print(val)
    
if __name__=='__main__':
    main()