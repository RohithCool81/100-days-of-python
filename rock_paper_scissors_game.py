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
name = input("Enter your name: ")
play_again = "yes"

while play_again == "yes":

    user_score = 0
    comp_score = 0

    while 1:

        best_of = int(input("Best of? : "))

        if best_of > 0 and best_of%2 != 0:
            break
        else:
            print("Please enter a positive odd number!")

    wins_needed = (best_of//2) + 1

    print("0: Rock, 1: Paper, 2: Scissors\n")
    while comp_score < wins_needed and user_score < wins_needed:
        user_choice = int(input("Enter your choice: "))

        if user_choice < 0 or user_choice > 2:
            print("Invalid choice!")
            continue
        else:
            comp_choice = random.randint(0, 2)

            print("\nYou chose:")
            print(art[user_choice])

            print("Computer chooses:")
            print(art[comp_choice])

            if user_choice == comp_choice:
                print("It's a draw!")
            elif (user_choice == 0 and comp_choice == 2) or (user_choice == 1 and comp_choice == 0) or (user_choice == 2 and comp_choice == 1):
                print("You win this round!")
                user_score+=1
            else:
                print("Computer wins this round")
                comp_score+=1
            print("\nSCOREBOARD")
            print(f"You: {user_score} | Computer: {comp_score}")

    if user_score>=wins_needed:
        print(f"{name}, You win!")
        print(f"Final Score: {name}| {user_score} - {comp_score} |Computer")
    elif comp_score>=wins_needed:
        print("Computer wins!")
        print(f"Final Score: Computer| {comp_score} - {user_score} |{name}")
    else:
        print("It's a tie!")
    
    play_again = input("Play again? (yes/no): ").lower()

print("Thanks for playing!")