# Python program to swap two variables

x = 5
y = 10

temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


# without temp varible.

a=56
b=45
a,b=b,a
print("A=",a)
print("B=",b)
