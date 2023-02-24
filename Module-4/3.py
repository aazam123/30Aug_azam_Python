#Write a Python program to read first n lines of a file.

n=int(input("Enter n lines "))
f=open("file1.txt","r")
for line in (f.readlines()[n:]):
    print(line,end=" ")
f.close()    


#  Write a Python program to read last n lines of a file.
n=int(inpur("Enter n line"))
f=open("file1.txt","r")
for line in (f.readlines()[-n]):
    print("line",end=" ")
f.close()    