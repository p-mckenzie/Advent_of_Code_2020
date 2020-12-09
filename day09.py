def part_1(data, lookback_window):
	'''Rolls through data, finds the invalid instance where the element is not the sum 
	of 2 previous numbers in the lookback_window'''
	
	# initialize lookback_window * lookback_window sized array with the sums of all elements
	rolling_sums = np.add.outer(data[:lookback_window], data[:lookback_window])

	# iterate through elements after the lookback_window, checking that each is in the sums, and updating
	for i in range(lookback_window, data.shape[0]):
		
		if data[i] not in rolling_sums:
			return i
			
		# update sums as we move along the data
		rolling_sums = np.vstack([rolling_sums[1:], (data[i] + data[i-lookback_window:i])])
		
def part_2(data, invalid):
	'''Starting at 0, iterates through expanding windows, looking for a window that the sum
	of all elements equal the invalid element.
	Returns the sum of the min and max element in this window.
	'''

	for start in range(invalid):
		cum_sum = 0
		goal = data[invalid]
		for i in range(start, invalid):
			if cum_sum<goal:
				cum_sum += data[i]
				if cum_sum==goal:
					return (data[start:i].min()+data[start:i].max())
			else:
				break
				
def main():
	with open('day09.txt', 'r') as f:
		txt = f.read().strip()
	f.close()

	data = np.array(txt.split(), dtype=np.int64)
	lookback_window = 25
		
	invalid = part_1(data, lookback_window)
	print(data[invalid])
	
	print(part_2(data, invalid))
	
if __name__=='__main__':
	import numpy as np
	main()