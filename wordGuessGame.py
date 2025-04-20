
# wordguessgame()
import random
import string
from words import words

def get_validword(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def word_guessing_game():
    word = get_validword(words).upper()
    word_letters = set(word)  # Letters in the word
    alphabet = set(string.ascii_uppercase) # All uppercase alphabets
    used_letters = set() # What the user has guessed
    
    lives = 6  # Number of incorrect guesses allowed

    while len(word_letters) > 0 and lives > 0:
        # Letters used by the user
        print("You have", lives, "lives left. Used letters:", ' '.join(used_letters))
        
        # Current word status (e.g., "p-th-n")
        word_display = ''.join([letter if letter.upper() in used_letters else '-' for letter in word])
        print(word_display)
        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Correct guess!")
            else:
                lives -= 1  # Takes away a life
                print('Letter is not in the word.')

        elif user_letter in used_letters:
            print("You have already used that character.")
        else:
            print('Invalid character. Try again.')

    # Game over conditions
    if lives == 0:
        print('You ran out of lives. Sorry, the word was', word)
    else:
        print('Congratulations! You guessed the word', word, '!')


    play_again = input("Do you want to play again? (YES/NO): ").upper()
    if play_again == "YES":
        word_guessing_game()  # Restart the game
    else:
      print("Thanks for playing!")


# Start the game
print("Welcome to the Word Guessing Game!")
word_guessing_game()