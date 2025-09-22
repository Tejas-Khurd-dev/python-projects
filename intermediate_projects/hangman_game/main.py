import random
import hangman_words
from hangman_art import stages, logo

def play_game():
    print(logo)
    print("🎮 Let us play Hangman! All words are fruit names 🍎🍌🥭")

    # Choose a random word
    chosen_word = random.choice(hangman_words.fruits_list)
    word_length = len(chosen_word)

    # Game variables
    lives = 6
    game_over = False
    correct_letters = []

    # Initial placeholder
    display = "_" * word_length
    print(f"Word to guess: {display} there are {len(chosen_word)} letters in these word")

    while not game_over:
        print(f"\n**************************** ❤️ {lives}/6 LIVES LEFT ****************************")
        guess = input("🔤 Guess a letter: ").lower()

        # Validation for wrong input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid letter.")
            continue

        # If already guessed
        if guess in correct_letters:
            print(f"🔁 You have already guessed '{guess}'")
            continue

        # Build display
        new_display = ""
        for letter in chosen_word:
            if letter == guess:
                new_display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                new_display += letter
            else:
                new_display += "_"

        # Check if guess was correct
        if guess in chosen_word:
            print(f"✅ Good job! You guessed a correct letter: '{guess}'")

        display = new_display
        print("📖 Word to guess: " + display)


        if guess not in chosen_word:
            lives -= 1
            print(f"❌ You guessed '{guess}', that's not in the word. You lose a life 💔 Now you have only {lives} ❤️ left.")
            if lives == 0:
                game_over = True


        print(stages[lives])

        if lives == 0:
            print(f"💀 Game Over! It was '{chosen_word}'. YOU LOSE 😢")

        if "_" not in display:
            game_over = True
            print("🏆🎉 **************************** YOU WIN **************************** 🎉🏆")

while True:
    user_input = input("Do you want to play hangman game type 'y' or 'n': ")

    if user_input == 'y':
        play_game()
    elif user_input == 'n':
        print("By👋! see you next time")
        break
    else:
        print("Invalid input! please enter valid input")
    
