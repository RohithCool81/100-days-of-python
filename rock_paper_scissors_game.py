
import random
print("Welcome to the Rock, Paper, Scissors game!\n")

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

art = [rock, paper, scissors]

print("0: Rock, 1: Paper, 2: Scissors\n")

user_choice = int(input("Enter your choice: "))

if user_choice < 0 or user_choice > 2:
    print("Invalid choice!")
else:
    comp_choice = random.randint(0, 2)

    print("\nYou chose:")
    print(art[user_choice])

    print("Computer chooses:")
    print(art[comp_choice])

    if user_choice == comp_choice:
        print("It's a draw!")
    elif (user_choice == 0 and comp_choice == 2) or (user_choice == 1 and comp_choice == 0) or (user_choice == 2 and comp_choice == 1):
        print("You win!")
    else:
        print("You lose!")