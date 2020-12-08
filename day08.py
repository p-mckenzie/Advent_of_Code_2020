class HandHeldBrain():
    def __init__(self, data):
        self.accumulator = 0
        self.index = 0
        self.instructions = data
        
    def process_line(self):
        command, interval = self.instructions[self.index].split()
        interval = int(interval)
        
        if command=='nop':
            self.index += 1
        elif command=='acc':
            self.accumulator += interval
            self.index += 1
        elif command=='jmp':
            self.index += interval
        return
    
    def run(self):
        already_executed = set()
            
        while self.index<len(self.instructions):
            self.process_line()
            if self.index in already_executed:
                return False
            else:
                already_executed.add(self.index)
        return True
    
    def __repr__(self):
        return 'Acc {} at index {}'.format(self.accumulator, self.index)
		
def main():
	# read data
	with open('day08.txt', 'r') as f:
		txt = f.read().strip()
	f.close()

	data = txt.split('\n')
			
	# part 1
	brain = HandHeldBrain(data.copy()) # initialize brain with input data
	brain.run() # run it until loop (controlled in HandHeldBrain.run())
	print(brain.accumulator)

	# part 2
	## (iterates through input commands, tries to change a single one each time)
	for i in range(len(data)):
		brain = HandHeldBrain(data.copy()) #initialize new instance of brain
		
		# switch jmp/nop if applicable
		if 'jmp' in brain.instructions[i]:
			brain.instructions[i] = brain.instructions[i].replace('jmp', 'nop')
		elif 'nop' in brain.instructions[i]:
			brain.instructions[i] = brain.instructions[i].replace('nop', 'jmp')
		else:
			# no need to run, loop again
			continue
			
		if brain.run():
			# if this is True, program completed successfully (no infinite loop)
			# otherwise, will continue to next
			break
			
	print(brain.accumulator)
	
if __name__=='__main__':
	main()