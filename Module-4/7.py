# Write a Python program to count the number of lines in a text file.
f= open("file1.txt","r")
count=0
line=f.readlines()
# print(line)
for i in line:
    if i:
        count+=1
print("number of lines",count)        
