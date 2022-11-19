#Write a Python program to get the Factorial number of given number.


num = int(input("enter a value  : " ))
f=1
for i in range(1, num+1):
    f=f*i
print("The factorial of",num,"is",(f))