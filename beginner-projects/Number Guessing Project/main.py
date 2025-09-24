import random
import art


def taking_input():
    print("🎯 Welcome to the Number Guessing Game! 🎯")
    print("🤔 I am thinking of a number between 1 and 100...")
    random_number = random.randint(1, 100)

    while True:
        difficulty = input("Choose difficulty: Type 'easy' 😎 or 'hard' 💀: ").lower()
        if difficulty == "easy":
            print("😌 You have 10 attempts! Good luck 🍀")
            return random_number, 10
        elif difficulty == "hard":
            print("😱 You have only 5 attempts! Be careful ⚡")
            return random_number, 5
        else:
            print("❌ Invalid input, please type 'easy' or 'hard'.")


def play_game():
    print(art.logo)
    random_number, attempts = taking_input()

    while attempts > 0:
        try:
            user_input_number = int(input("👉 Guess a number: "))
        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")
            continue

        if user_input_number > random_number:
            print("⬆️ Too high 📈")
        elif user_input_number < random_number:
            print("⬇️ Too low 📉")
        else:
            print("🎉✨ You made a correct guess! 🏆🎯")
            return

        attempts -= 1
        print(f"⏳ {attempts} attempts left")

    # If loop ends → user ran out of attempts
    print("💀 All attempts are used, You Lose ❌")
    print(f"The number was {random_number}")


def start():
    while True:
        play_game()
        again = input("🔁 Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("👋 Thanks for playing! See you next time 🎯")
            break


start()
