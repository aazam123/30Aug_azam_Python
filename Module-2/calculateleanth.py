#Python program to calculate the length of a string

def findLen(str):
    counter = 0   
    for i in str:
        counter += 1
    return counter
 
 
str = "geeks"
print(findLen(str))
