def main():
    with open('day14.txt', 'r') as f:
        txt = f.read().strip()
    f.close()

    from re import findall
    from itertools import product

    memory1 = {}
    memory2 = {}

    for line in txt.split('\n'):
        if line.startswith('mask'):
            # update bitmask with current values
            mask = line.rsplit(maxsplit=1)[-1]
        else:
            # update memory location
            location, value = findall('\d+', line)
            location = '{0:036b}'.format(int(location))
            value = '{0:036b}'.format(int(value))

            # part 1 - update value, leave location as-is
            memory1[location] = ''.join([value[i] if mask[i]=='X' else mask[i] for i in range(36)])

            # part 2 - update location with floating, leave value as-is
            location = ''.join([location[i] if mask[i]=='0' else '1' if mask[i]=='1' else mask[i] for i in range(36)])
            for replacements in product([0,1],repeat=location.count('X')):

                location_variation = location
                for replacement in replacements:
                    location_variation = location_variation.replace('X', str(replacement), 1)
                memory2[location_variation] = value
    # part 1
    print(sum([int(x, 2) for x in memory1.values()]))
    # part 2
    print(sum([int(x, 2) for x in memory2.values()]))
    
if __name__=='__main__':
    main()