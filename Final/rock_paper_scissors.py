# Rock Paper Scissors using If Elif.

print("ROCK PAPER SCISSORS")

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
ans = "yes"
while ans == "yes":
    user_choice = int(input("What you choose? Type 0 for rock, 1 for paper or 3 for Scissors.: \n"))
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 0:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You Win!")
    elif computer_choice == user_choice:
        print("It is a draw try agian ") 
    ans = input("Wanna try once more ?  (yes/no)")
