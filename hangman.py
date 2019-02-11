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
    
"""str="policeman"
print(get_masked_word(str))"""

def set_tries_left(tries):
    tries_left = (10 - tries)
    return tries_left


def type_guess_word(word_file, guess_word):
    word_file_list =[]
    guess_word_list =[]
    for i in word_file_list:
        word_file_list = word_file.append()
        print= input("input a char{guess_word}")
        if guess_word[i] == word_file_list[i]:
            return guess_word
        else:
            print("oops that not in this masked word, type next charecter")
    return word_file_list()
