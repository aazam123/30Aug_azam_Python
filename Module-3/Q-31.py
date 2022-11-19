#How will you create a dictionary using tuples in python?
data = ((24, "bobby"), (21, "ojsawi"))
# convert into dictionary
final = dict((value, key) for key, value in data)

print(final)
