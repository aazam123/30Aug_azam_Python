# Write python program that user to enter only odd numbers, else will raise an exception.



num =int(input("Enter the number"))
a= num%2

try:
    print("this number is odd")
except:
    print("this number is not odd")

