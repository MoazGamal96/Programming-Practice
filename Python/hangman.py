import random
import string
words = " "
def get_valid_word (words):
    words = random.choice(words) #randomly chose from list
    while '_' in words or ' ' in words :
        words = random.choice(words)
    return words
def hangman() :
    words = get_valid_word(words) #letters on the word
    words_letter = set(words)
    alphabet = set(string.ascii_uppercase)
    used_letter = set () #what the user has guessed

    #getting the user input 
    user_letter = input('Guess a letter: ').upper

user = input("writ something")
print(user)



