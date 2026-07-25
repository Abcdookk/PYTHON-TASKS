import random

def play_hangman():
    # Predefined list of 5 words
    words = ["python", "variable", "function", "string", "syntax"]
    target_word = random.choice(words)
    
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6
    
    print("Welcome to Hangman!")
    
    # While loop for game mechanics
    while incorrect_guesses < max_incorrect:
        # String manipulation
        display = ""
        for char in target_word:
            if char in guessed_letters:
                display += char + " "
            else:
                display += "_ "
                
        print(f"\nWord: {display}")
        
        # Check for win
        if "_" not in display:
            print("Congratulations! You guessed the word.")
            break
            
        # Basic console input/output
        guess = input("Guess a letter: ").lower().strip()
        
        # if-else logic
        if not guess or len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in target_word:
            print("Correct!")
            guessed_letters.append(guess)
        else:
            print("Incorrect guess.")
            guessed_letters.append(guess)
            incorrect_guesses += 1
            print(f"Guesses remaining: {max_incorrect - incorrect_guesses}")
            
    if incorrect_guesses == max_incorrect:
        print(f"\nGame Over! The word was: '{target_word}'")

if __name__ == "__main__":
    play_hangman()