#This is our first number guessing game

import random

#defining variables
n = random.randint(1,99)
guess = int(input("Enter an integer from 1 to 99 :"))
i = 0

while n!=guess:
    #print("Wrong number guessed .\n Please try again")
    if guess < n:
        print("Your guessed number is lower than the original number")
        guess = int(input("Enter an integer from 1 to 99 :"))
        i+=1
    else:
        print("Your guessed number is greater than the original number")
        guess = int(input("Enter an integer from 1 to 99 :"))
        i+=1
        
print("Congratulations !!! Your guess is correct .")
print("Number of attempts taken is",i)
    
        
        
