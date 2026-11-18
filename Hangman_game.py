import random


words = ["computer","server","cursor","launcher","trigger"]

SECRET_WORD = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_attempts = 6


print("\n---- Welcome to Hangman Game World! ----")

while incorrect_guesses < max_attempts:

    display_word = ''

    for letter in SECRET_WORD:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\n Word:", display_word)
    print("Incorrect guess:",max_attempts - incorrect_guesses)

    if all(letter in guessed_letters for letter in SECRET_WORD):
        print("Congratulations! You've guessed the word:", SECRET_WORD)
        break

    guess = input("Guess a letter: ").lower().strip()    
    
    if len(guess) !=1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    guessed_letters.append(guess)

    if guess not in SECRET_WORD:
        incorrect_guesses += 1
        print("Incorrect guess!")
else:
    print("\nSorry, you've run out of attempts. The word was:", SECRET_WORD)
