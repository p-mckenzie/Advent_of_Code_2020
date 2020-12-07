class Bag():
    def __init__(self, bag_name, quantity):
        '''Stores useful information and can yield sub-bags 
		(aka "look inside back to see how many of what kind of bag is in there"
		'''
        
        self.bag_name = bag_name # this bag's name 
        self.quantity = quantity # the quantity of this bag
        self.sub_bag_count = 0 # the number of bags each of this bag contains
        self.i = -1 # placeholder to iterate through bags that this bag contains
        
    def get_next(self, quantity):
        # yields the next bag (using i) that this bag contains
        
        if len(quantity[self.bag_name][self.i+1])>0:
            self.i += 1
            return quantity[self.bag_name][self.i]
        else:
            raise IndexError("Reached root of path.")
            
    
    def __repr__(self):
        return '{} {} after {} lookups'.format(self.quantity, self.bag_name, self.i)
    
    def __str__(self):
        return '{} {} after {} lookups'.format(self.quantity, self.bag_name, self.i)
		
def part_1(contain, goal='shiny gold'):
    processed = set()
    to_process = contain[goal]

    while len(to_process)>0:
        new = set()
        for item in to_process:
            new = new.union(contain[item])
            processed.add(item)

        to_process = new-processed
    return len(processed)
	
def part_2(quantity, start='shiny gold'):
    '''Expands possible paths start until there are no more sub-bags, then works back towards start, summing
    the # of bags each bag contains. Eventually paths should be a list with a single element in it (the start Bag),
    where that bag's attribute sub_bag_count is the # of bags contained inside the entire structure.
    '''
    
    # initiates path based on input start
    path = []
    path.append(Bag(start, 1))
    
    
    while True:
        try:
            # expands path by iterating to find "root" - where bag contains no more bags
            # path will contain instances of Bag class (to store relevant information)
            while True:
                try:
                    bag, qty = path[-1].get_next(quantity)
                    path.append(Bag(bag, qty))
                except IndexError as e:
                    # found the root
                    break

            # now that the path has been expanded, "delete" the last entry 
            ## (aka count how many bags are in last, add that as "sub_bag_count" to the second to last, then pop)
            path[-2].sub_bag_count += path[-2].quantity*(path[-1].quantity + path[-1].sub_bag_count)
            path.pop(-1)
            
        except IndexError:
            # error here indicates the Bag iterator at path[0] has no more sub-bags to look in
            break
            
    # there should only be one Bag left - return the number of bags it contains
    assert len(path)==1
    return path[0].sub_bag_count
	
def main():
	# read data
	with open('day07.txt', 'r') as f:
		txt = f.read().strip()
	f.close()

	from collections import defaultdict

	# maps a bag to the set of bags that could contain it
	contain = defaultdict(set)

	# maps a bag to the (bag, quantity) pairs that it contains
	quantity = defaultdict(list)

	from re import findall

	# iterate through rules once, create data structures to be used in pt. 1 and pt. 2
	for rule in txt.split('\n'):
		bags = findall(r"\d* *\w+ \w+(?= bag)", rule)
		contains = bags[0]
		for i in range(1, len(bags)):
			qty, bag = bags[i].split(maxsplit=1)
			
			if qty=='no':
				continue
			
			# for part 1
			contain[bag].add(contains)
			
			# for part 2
			quantity[contains].append((bag, int(qty)))
			
	# part 1
	print(part_1(contain))

	# part 2
	print(part_2(quantity))
	
if __name__=='__main__':
	main()