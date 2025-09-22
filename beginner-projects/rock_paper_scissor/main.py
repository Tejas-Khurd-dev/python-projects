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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_list = ["rock", "Paper", "Scissor"]
game_images = [rock, paper, scissor]
is_True = True

while is_True:
    print("Welcome to the ROCK ✊ PAPER ✋ SCISSORS ✌️ Game\n")

    try:
        user_choice = int(input("Enter your choice: 0 for Rock, 1 for Paper, 2 for Scissors, 3 to End: "))
    except ValueError:
        print("Invalid input! Please enter a number (0, 1, 2, or 3).")
        continue

    if user_choice == 3:
        is_True = False
        continue

    if 0 <= user_choice < 3:
        print(f"\nYour Choice is {game_list[user_choice]}:")
        print(game_images[user_choice])

        computer_choice = random.randint(0, 2)
        print(f"\nComputer Choice is {game_list[computer_choice]}:")
        print(game_images[computer_choice])

        if user_choice == computer_choice:
            print("\n*** It's a Tie ***")
        elif (user_choice == 0 and computer_choice == 2) or \
            (user_choice == 1 and computer_choice == 0) or \
            (user_choice == 2 and computer_choice == 1):
            # That '\' is the line continuation character in Python.
            # It tells Python:
            # "This statement continues on the next line — don’t treat the newline as the end of the statement."
            print("\n*** You Win ***")
        else:
            print("\n*** Computer Wins ***")

    else:
        print("Wrong choice, please enter a valid number (0, 1, 2 or 3).")
