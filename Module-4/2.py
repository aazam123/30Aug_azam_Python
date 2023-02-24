# Write a Python program to append text to a file and display the text.
from asyncore import write


f=open("file1.txt","a")
f.write("one\n",)
f.close()