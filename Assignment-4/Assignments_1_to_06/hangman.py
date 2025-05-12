import random

words = ["python", "developer", "hangman", "challenge", "coding"]
word = random.choice(words) 
guessed_word = ["_"] * len(word)  
attempts = 6  
guessed_letters = []

print("Welcome to Hangman! Guess the word.")

while attempts > 0 and "_" in guessed_word:
    print("Word: " + " ".join(guessed_word))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")

if "_" not in guessed_word:
    print(f"🎉 You won! The word was '{word}'.")
else:
    print(f"❌ You lost! The word was '{word}'.")
