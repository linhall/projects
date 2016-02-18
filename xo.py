def xo(s):
	num_X = 0
	num_O = 0
	for i in s:
		i = i.lower()
		if 'x' in i:
			num_X += 1
		if 'o' in i:
			num_O += 1
	if num_X == num_O:
		return True
	else:
		return False



print xo('xxxxoOOooo')
print xo('xxoo')