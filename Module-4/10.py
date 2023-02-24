# Write a Python program to copy the contents of a file to another file. 
f1= open("file1.txt","r")
f2 =open("file2.txt","w")
# print(f1.readlines())
data=f1.readlines()
for line in data:
    f2.write(line)
f1.close()    
f2.close()