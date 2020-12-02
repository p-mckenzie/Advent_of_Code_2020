def validate_passwords(data):
    num_valid_1 = 0
    num_valid_2 = 0

    # extract relevant information
    for datum in data:
        rng, token, pswd = datum.split()

        # remove hyphen
        token = token[:-1]
        # convert range to integer values
        rng = [int(x) for x in rng.split('-')]

        # number of occurrences of token in pswd
        cnt = pswd.count(token)

        # pt 1 is valid if count is within the range
        if cnt>=rng[0] and cnt<=rng[1]:
            num_valid_1 += 1

        # pt 2 is valid if token appears at only one of the rng locations
        if ((pswd[rng[0]-1]==token) + (pswd[rng[1]-1]==token))==1:
            num_valid_2 += 1
            
    return num_valid_1, num_valid_2
	
def main():
    # read data into text
    with open('day02.txt', 'r') as f:
        txt = f.read().strip()
    f.close()
    
    # split into individual lines
    data = txt.split('\n')
    
    # parse
    pt1, pt2 = validate_passwords(data)
    
    print(pt1)
    print(pt2)
	
if __name__=='__main__':
	main()