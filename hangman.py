 # hangman.py

import random

def get_secret_word(word_file="/usr/share/dict/words"):
    with open(word_file) as f:
        good_words = []
        for i in f:
            i = i.strip()
            if len(i) <= 6:     # No short words
                continue
            if not i.isalpha(): # No punctuation
                continue
            if i[0].isupper():  # No proper nouns
                continue
            good_words.append(i)
    return random.choice(good_words)

def get_masked_word(word_file):
        mask_word="*" * len(word_file)
        return mask_word
str="asdfgh"
print(get_masked_word(str))
"""def set_tries_left(word_file=""):
    with open(word_file) as f:
        tries =10
        for tries in range(0, -1):
            print=input("enter guess word",guess)
            input(read.word())
            tries = tries -1
    return(tries)

def input_letter(word_file, input_letter):
    guess_word_list=[word_file]
    for i in guess_word:"""
        
    
