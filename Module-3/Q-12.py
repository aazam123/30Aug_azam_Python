#Write a Python program to convert a list of characters into a string

def convert(s):

	
	new = ""
	for x in s:
		new += x

	return new
	
s = ['A', 'Z', 'A', 'M', 'M', 'O', 'R', 'V', 'A', 'D', 'I', 'Y', 'A']
print(convert(s))
