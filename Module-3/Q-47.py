#Write a Python program to create a dictionary from a string.
st = input("Enter a string: ")
dic = {} #creates an empty dictionary
for ch in st:
    if ch in dic: #if next character is already in the dictionary
        dic[ch] += 1
    else:
        dic[ch] = 1 #if ch appears for the first time
for key in dic:
    print(key,':',dic[key])
