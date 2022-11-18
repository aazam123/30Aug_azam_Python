#Write a Python program to convert a tuple to a string
def convertTuple(tup):
		# initialize an empty string
	str = ''
	for item in tup:
		str = str + item
	return str


# Driver code
tuple = ('A', 'a', 'z', 'a', 'm')
str = convertTuple(tuple)
print(str)

