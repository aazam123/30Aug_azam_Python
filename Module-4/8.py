# Write a Python program to count the frequency of words in a file. 
f=open("file1.txt","r")
word=input("Enter the word to be search")
s=f.read()
lst=s.split()
count=0
for i in lst:
    if i==word:
        count+=1
print("word {} times {}".format(word,count))        

