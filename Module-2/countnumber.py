#Python program to count the number of characters (characterfrequency) in a string

string = "The best of both worlds";  
count = 0;  
   
 
for i in range(0, len(string)):  
    if(string[i] != ' '):  
        count = count + 1;  
    
print("Total number of characters in a string: " + str(count));  