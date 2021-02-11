def part_1(voltages):
	ranges = {1:0, 2:0, 3:0}

	# go element to element, count the voltage jump in ranges
	for i in range(1,len(voltages)):
		jump = voltages[i]-voltages[i-1]
		ranges[jump] += 1
		
	return ranges[1]*ranges[3]
	
def part_2(voltages):
	# paths[i] is how many different ways there are to get to voltages[i]
	paths = [1] + [0] * (len(voltages) - 1)

	for i, volt in enumerate(voltages):
		# at most the 3 previous voltages could connect to current voltage
		for j in range(i - 3, i):
			# if voltages[j] is in range of volt, then all the ways to get to voltages[j] are ways to get to volt
			if(volt - voltages[j] <= 3):
				# sum up to 3 paths
				paths[i] += paths[j]
				
	return paths[-1] # how many different ways to get to last entry (goal)

def main():
	with open('day10.txt', 'r') as f:
		txt = f.read().strip()
	f.close()

	voltages = sorted([int(x) for x in txt.split()])

	# add in start and end points
	voltages = [0]+voltages+[voltages[-1]+3]
	
	print(part_1(voltages))
	print(part_2(voltages))


if __name__=='__main__':
	main()