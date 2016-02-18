def disemvowel(string):
	vowel = ['a', 'e', 'i', 'o', 'u']
	new_String = []
	for v in string:
		if v.lower() not in vowel:
			new_String.append(v)
	return "".join(new_String)




print disemvowel("This website is for losers, LOL!")