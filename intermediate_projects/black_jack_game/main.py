import random
import art

cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

def convert_cards_to_values(cards_list):
    """Convert card names to numerical values."""
    for i in range(len(cards_list)):
        if cards_list[i] == "Ace":
            cards_list[i] = 11
        elif cards_list[i] in ["King", "Queen", "Jack"]:
            cards_list[i] = 10
    return cards_list

def convert_ace_to_1(cards_list):
    """Convert Ace from 11 to 1 if total exceeds 21."""
    for card in cards_list:
        if sum(cards_list) > 21 and 11 in cards_list:
            ace_index = cards_list.index(card)
            cards_list[ace_index] = 1

def black_jack_check(cards_list):
    """Check if the hand is a Blackjack."""
    return len(cards_list) == 2 and 11 in cards_list and 10 in cards_list

def print_black_jack_winner(user_cards, computer_cards):
    """Determine if there is a Blackjack winner."""
    black_jack_user = black_jack_check(user_cards)
    black_jack_computer = black_jack_check(computer_cards)

    if black_jack_user and black_jack_computer:
        return "Tie"
    elif black_jack_user:
        return "User_Wins"
    elif black_jack_computer:
        return "Computer_Wins"
    else:
        return None

def taking_input():
    """Deal initial cards and show user's hand and dealer's first card."""
    user_cards = [random.choice(cards), random.choice(cards)]
    print(f"\n🎴 Your cards: {user_cards}", end=" ")
    convert_cards_to_values(user_cards)
    print(f"| Total score: {sum(user_cards)}")

    computer_cards = [random.choice(cards), random.choice(cards)]
    print(f"🤖 Dealer shows: {computer_cards[0]}")
    convert_cards_to_values(computer_cards)

    return user_cards, computer_cards

def computer_score_great_than_17(computer_cards):
    """Dealer draws until reaching at least 17."""
    while sum(computer_cards) < 17:
        computer_cards.append(random.choice(cards))
        convert_cards_to_values(computer_cards)
        convert_ace_to_1(computer_cards)
    return computer_cards

def compare_score(user_cards, computer_cards):
    """Compare final scores and print the result."""
    print("\n🏁 Final Results:")
    print(f"Your final hand: {user_cards} | Final score: {sum(user_cards)}")
    print(f"Dealer's final hand: {computer_cards} | Final score: {sum(computer_cards)}\n")

    if sum(user_cards) > 21:
        print("💥 You busted! Dealer wins!")
    elif sum(computer_cards) > 21:
        print("🎉 Dealer busted! You win!")
    elif sum(user_cards) > sum(computer_cards):
        print("🏆 Congratulations! You win!")
    elif sum(user_cards) < sum(computer_cards):
        print("🤖 Dealer wins! Better luck next time.")
    else:
        print("🤝 It's a draw!")

def play_game():
    """Run a single round of Blackjack."""
    user_cards, computer_cards = taking_input()

    black_jack_result = print_black_jack_winner(user_cards, computer_cards)
    if black_jack_result == "Tie":
        print("\n🃏 Black Jack Tie! What a close game!")
        return
    elif black_jack_result == "User_Wins":
        print("\n✨ Black Jack! You won instantly! Congrats!")
        return
    elif black_jack_result == "Computer_Wins":
        print("\n🤖 Dealer got Black Jack! You lose!")
        return

    computer_cards = computer_score_great_than_17(computer_cards)

    while True:
        if sum(user_cards) > 21:
            print("\n💥 You busted! Dealer wins!")
            break
        elif sum(computer_cards) > 21:
            print("\n🎉 Dealer busted! You win!")
            break

        user_choice = input("\nDo you want another card? Enter 'y' or 'n': ").lower()
        if user_choice == "y":
            user_cards.append(random.choice(cards))
            print(f"\n🎴 Your cards: {user_cards}")
            convert_cards_to_values(user_cards)
            convert_ace_to_1(user_cards)
            print(f"\n🎴 Your cards after converting into values: {user_cards} | Current score: {sum(user_cards)}")
            print(f"🤖 Dealer shows after converting into values: {computer_cards[0]}")
        elif user_choice == "n":
            break
        else:
            print("❌ Invalid input. Please enter 'y' or 'n'.")

    compare_score(user_cards, computer_cards)

while True:
    game_choice = input("\n🎮 Play a game of Blackjack? 'y' or 'n': ").lower()
    if game_choice == "y":
        print(art.logo)
        play_game()
    elif game_choice == "n":
        print("\n👋 Thanks for playing! Goodbye!")
        break
    else:
        print("❌ Invalid input. Please enter 'y' or 'n'.")
