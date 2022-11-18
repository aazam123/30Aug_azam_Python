#Why Do You Use the Zip () Method in Python?
"""Python zip() method takes iterable or containers and returns a single iterator object, having
 mapped values from all the containers. It is used to map the similar index of multiple containers
so that they can be used just using a single entity."""

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
 
# using zip() to map values
mapped = zip(name, roll_no)
 
print(set(mapped))