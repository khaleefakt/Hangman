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

def get_guess_word(word_file="/usr/share/dict/words"):
    with open(word_file) as f:
        f=word_file
        f='*' * len(word_file)
    return(word_file)

def set_tries_left(word_file="/usr/share/dict/words"):
    with open(word_file) as f:
        tries =10
        for tries in range(0, -1):
            print=input("enter guess word",guess)
            input(read.word())
    return(tries)
