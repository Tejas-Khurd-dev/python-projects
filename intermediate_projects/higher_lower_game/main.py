import random
import art
from game_data import data


def format_account(account):
    """Return formatted account string for printing with emoji."""
    return f"{account['name']} {art.get_emoji(account)} — {account['description']} from {account['country']}"

def play_game():
    score = 0
    game_should_continue = True

    account_1 = random.choice(data)
    account_2 = random.choice(data)
    while account_2 == account_1:
        account_2 = random.choice(data)

    while game_should_continue:
        print(art.logo)
        if score > 0:
            print(f"🎉 You're right! Current score: {score} 🎉\n")

        print(f"Compare A: {format_account(account_1)}")
        print(art.vs)
        print(f"Against B: {format_account(account_2)}")

        while True:
            user_choice = input("Who has more followers? Type 'A' or 'B' 🤔: ").lower()
            if user_choice in ["a", "b"]:
                break
            print("❌ Invalid input! Please type 'A' or 'B'.")

        a_followers = account_1['follower_count']
        b_followers = account_2['follower_count']

        if (user_choice == "a" and a_followers > b_followers) or (user_choice == "b" and b_followers > a_followers):
            score += 1

            winner = account_1 if a_followers > b_followers else account_2
            print(f"🔥 {winner['name']} has more followers! 🔥")

            account_1 = account_2
            account_2 = random.choice(data)
            while account_2 == account_1:
                account_2 = random.choice(data)

            print("\n" * 3)
        else:
            print(f"\n💔 Sorry, that's wrong. Final score: {score} 💔")
            game_should_continue = False


while True:
    play_game()

    while True:
        restart_game = input("Do you want to retry? Type 'y' for yes or 'n' for no: ").lower()

        if restart_game == 'y':
            break
        elif restart_game == 'n':
            print("By by!")
            exit()
        else:
            print("Invalid input please type 'y' or 'n'")
            continue
    
