import random

def hangman():
    words = ["apple", "banana", "cherry", "dragonfruit", "elderberry", "fig", "grape"]
    word = random.choice(words)
    guessed_letters = set()

    attempts = 6
    while attempts > 0:
        guessed_word = ""
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += "_"

        print(f"Word: {guessed_word}")
        print(f"Attempts left: {attempts}")

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            attempts -= 1

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word!")
            break

    if attempts == 0:
        print("Sorry, you ran out of attempts. Game over!")
    else:
        print("Thanks for playing!")

