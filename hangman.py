import random
from word import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly ghooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word.upper()
    
    
def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the world
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    # getting user input
    while len(word_letters) > 0:
        print('You have used these letters: ', ' '.join(used_letters))
        
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)             
        elif user_letter in used_letters:
            print('You have already used that letter. Try again')           
        else:
            print('Invalid character. Try again')


print(hangman())