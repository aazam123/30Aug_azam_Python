#Write a Python program to reverse a tuple. 
def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup
      

tuples = ('A','a','z','a',' ','m','m','o','v','a','d','i','y','a',)
print(Reverse(tuples))