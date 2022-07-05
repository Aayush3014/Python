#Number guessing game using if elif.

print("""
\t\t<<<<<<------Welcome to the number Guessing Game!!!!------>>>>>>
\t\t<<<<<<------Guess the number in First Three attempts to Win------>>>>>>
""")

import random

a = random.randint(0,100)

count = 1

ans = "y"

while ans == "y":
    
    guess = int(input("Guess a number between 1 and 100 : "))
    
    
    if guess < a:
        
        if guess < a-20:
            
            print("Your guess is too low.")
            count += 1
        
        else:
            
            print("your guess is low.")
            count += 1
    
    elif guess > a:
        
        if guess > a+20:
            
            print("Your guess is too high.")
            count += 1
        
        else:
            
            print("your guess is high.")
            count += 1
    
    elif guess == a:
        
        if count == 1:
            
            print("Congratulations. You won the First prize.")
            print("You guessed the number in first attempt.")
            break
        
        elif count == 2:
            
            print("Congratulations. You won the Second prize.")
            print("You guessed the number in second attempt.")
            break
        
        elif count == 3:
            
            print("Congratulations. You won the Third prize.")
            print("You guessed the number in third attempt.")
        
        else:
            
            print(f"Congratulations.You guessed the correct number.")
            print(f"You took {count} Guesses.")
            break
    
    ans = input("Wanna give it a try ? (y/n) ")

print("""Come Again to try your luck!!!!""")