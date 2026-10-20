import random
words=[
    "python",
    "computer",
    "database",
    "developer",
    "analysis"
]

word=random.choice(words)

print(word)

hangman_art=[
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

print("Welcome to Hangman!")
print(hangman_art[0])

while attempts > 0:
    guess=input("Enter a letter: ").lower()

    if len(guess)!= 1 or not guess.isalpha():
        print("Enter one letter only.")
        continue