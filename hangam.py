# hangman.py

import random

# Word list (you can replace this with the downloaded txt file)
words = [
    "python",
    "computer",
    "developer",
    "algorithm",
    "database",
    "programming",
    "machine",
    "analysis"
]

# ASCII Hangman stages
hangman_art = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,

    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,

    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,

    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,

    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,

    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,

    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]


def display_word(word, guessed_letters):
    result = ""

    for letter in word:
        if letter in guessed_letters:
            result += letter.upper() + " "
        else:
            result += "_ "

    return result


def play_game():

    word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = set()

    attempts = 6

    print("🎮 Welcome to Hangman Game!")
    print("Guess the word before the man is hanged!")
    print(hangman_art[0])


    while attempts > 0:

        print("\nWord:", display_word(word, guessed_letters))
        print("Guessed letters:", " ".join(wrong_guesses))
        print("Remaining attempts:", attempts)

        guess = input("Enter a letter: ").lower()


        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.")
            continue


        # Duplicate guess check
        if guess in guessed_letters or guess in wrong_guesses:
            print("You already guessed that letter!")
            continue


        # Correct guess
        if guess in word:
            guessed_letters.add(guess)
            print("✅ Correct guess!")

        # Wrong guess
        else:
            wrong_guesses.add(guess)
            attempts -= 1
            print("❌ Wrong guess!")
            print(hangman_art[6 - attempts])


        # Check victory
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You won!")
            print("The word was:", word.upper())
            return


    # Game over
    print("\n💀 Game Over!")
    print("The correct word was:", word.upper())


play_game()