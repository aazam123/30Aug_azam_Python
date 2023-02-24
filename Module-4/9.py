# Write a Python program to write a list to a file.
from distutils.text_file import TextFile


Fruit_list =["Apple","mango","Banana","Cherry","Guavava","jackfruit","grapes"]
print(Fruit_list)
f=open("file2.txt","a")
print(f)
a= '\n'.join(Fruit_list)
f.writelines(a)