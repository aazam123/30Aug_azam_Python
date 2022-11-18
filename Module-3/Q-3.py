#Differentiate between append () and extend () methods 
fl=open("F:\Python\Assignment\Module-3\insertdata.txt","a")


id=input("Enter ID:")
nm=input("Enter Name:")

fl.write(f"ID:{id}\nName:{nm}\n")



prime_numbers = [2, 3, 5]

numbers = [1, 4]

numbers.extend(prime_numbers)

print('List after extend():', numbers)

