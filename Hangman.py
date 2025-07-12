import random

# Word list with hints
word_list = [
    ("elephant", "A large land animal with a trunk"),
    ("python", "A popular programming language"),
    ("guitar", "A musical instrument with strings"),
    ("ocean", "A large body of salt water"),
    ("banana", "A yellow fruit")
]

# Randomly choose a word and its hint
word, hint = random.choice(word_list)
word = word.lower()
guessed_letters = []
attempts = 6  # Total wrong guesses allowed

print("🎮 Welcome to Hangman!")
print(f"Hint: {hint}")
print("_ " * len(word))

# Game loop
while attempts > 0:
    guess = input("\nGuess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if the guess is correct
    if guess in word:
        print("✅ Correct guess!")
    else:
        print("❌ Wrong guess!")
        attempts -= 1
        print(f"Attempts remaining: {attempts}")

    # Show current progress
    progress = [letter if letter in guessed_letters else "_" for letter in word]
    print("Word: ", " ".join(progress))

    # Check for win
    if "_" not in progress:
        print("\n🎉 Congratulations! You've guessed the word:", word)
        break

# Check for loss
if attempts == 0:
    print("\n😢 Game Over! The word was:", word)
