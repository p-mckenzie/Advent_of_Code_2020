def eval_equal(subline):
	subline = subline.split()
	while len(subline)>1:
		subline = [str(eval(''.join(subline[:3])))] + subline[3:]
	return subline[0]
	
def eval_prioritized(subline):
	subline = subline.split()
	while '+' in subline:
		adds = subline.index('+')
		result = str(eval(''.join(subline[adds-1:adds+2])))

		subline = subline[:adds-1] + [result] + subline[adds+2:]

	return str(eval(''.join(subline)))
	
def eval_line(line, pt=1):
	from re import findall

	# parse parenthesis first
	while '(' in line or ')' in line:
		for subsection in findall(r'\([^()]+\)', line):
			if pt==1:
				line = line.replace(subsection, eval_equal(subsection[1:-1]))
			elif pt==2:
				line = line.replace(subsection, eval_prioritized(subsection[1:-1]))

	# parse overall expression
	if pt==1:
		return int(eval_equal(line))
	elif pt==2:
		return int(eval_prioritized(line))
	
	
def main():
	# read data
	with open('day18.txt', 'r') as f:
		txt = f.read().strip()
	f.close()

	# part 1
	print(sum([eval_line(line, pt=1) for line in txt.split('\n')]))

	# part 2
	print(sum([eval_line(line, pt=2) for line in txt.split('\n')]))
	
if __name__=='__main__':
	main()