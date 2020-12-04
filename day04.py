def validate_data(key, val):
	if key=='byr': # (Birth Year) - four digits; at least 1920 and at most 2002.
		return (len(val)==4 and val>='1920' and val<='2002')
	
	elif key=='iyr': # (Issue Year) - four digits; at least 2010 and at most 2020.
		return (len(val)==4 and val>='2010' and val<='2020')
		
	elif key=='eyr': # (Expiration Year) - four digits; at least 2020 and at most 2030.
		return (len(val)==4 and val>='2020' and val<='2030')
		
	elif key=='hgt': # (Height) - a number followed by either cm or in:
		if val.endswith('cm'):
			# If cm, the number must be at least 150 and at most 193.
			return (val[:3]>='150' and val[:3]<='193')
		elif val.endswith('in'):
			# If in, the number must be at least 59 and at most 76.
			return (val[:2]>='59' and val[:2]<='76')
		else:
			# something went hugely wrong
			#raise ValueError('Units for hgt field were incorrect ({}).'.format(key)) 
			return False
		
	elif key=='hcl': # (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
		valid_chars = 0
		for i,char in enumerate(val):
			if i==0 and char=='#':
				valid_chars += 1
			elif i>0 and ((char>='0' and char<='9') or (char>='a' and char<='f')):
				valid_chars += 1
				
		return (valid_chars==7)
			
	elif key=='ecl': # (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
		return (val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
		
	elif key=='pid': # (Passport ID) - a nine-digit number, including leading zeroes.
		return (len(val)==9 and val>='0'*9 and val<='9'*9)
		
	elif key=='cid': # (Country ID) - ignored, missing or not.
		return True
	
	else:
		# something went hugely wrong
		raise ValueError('An invalid data field was passed to validate_data ({}).'.format(key)) 
	
def main():
	# read data and store each row as a string, in a list
	with open('day04.txt', 'r') as f:
		txt = f.read().strip()
	f.close()
	
	entries = txt.split('\n\n')
	required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']) #'cid'
	
	valid_1 = 0
	valid_2 = 0

	for entry in entries:
		# iterate through individual passport data
		
		pswds = {}
		for info in entry.split():
			# store field, value pairs
			x,y = info.split(':')
			
			# to skip additional looping, validate now
			pswds[x] = validate_data(x,y)
			
			
		# check if all fields are present (ignoring CID)
		if len(required_fields - set(pswds.keys()))==0:
			valid_1 += 1
			
			# also check that all data values were valid
			if min(pswds.values()):
				valid_2 += 1
	
	# part 1
	print(valid_1)
	
	# part 2
	print(valid_2)
	
if __name__=='__main__':
	main()