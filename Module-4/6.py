# Write a python program to find the longest words.
f=open("file1.txt","r")
s=f.read()
seprt_word=s.split()
print(s)
#longest word
print(max(seprt_word,key=len))