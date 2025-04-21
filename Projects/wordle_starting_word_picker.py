import random

word_list = ["apple", "grape", "peach", "berry", "melon"]
hidden_word = random.choice(word_list)

for i in range(6):
    guess_word = input("Enter your guess (5 letters): ").lower()
    if len(guess_word) > 5 or len(guess_word) < 5:
        print("Please enter a 5-letter word. ")
        continue
    if guess_word == hidden_word:
        print("Congratulations! You've guessed the word!")
    else:
        print("That's not the word.")
        if guess_word[0] == hidden_word[0]:
            print("✅", end="")
   


# This code implements a simple Wordle game where the user has to guess a 5-letter word.
# The user has 6 attempts to guess the word, and feedback is provided for each guess.
# The feedback indicates whether the letters are in the correct position (G), in the word but wrong position (Y), or not in the word (B).