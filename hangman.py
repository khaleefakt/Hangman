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
    


def set_tries_left(tries):
   
    tries_left = (10 - tries)
    return tries_left


def type_guess_word(word_file, guess_word, guessed_line):
    if guess_word in word_file:
        x = 0
        for i in word_file:
            if i == guess_word:
                guessed_line = guessed_line [0:x] + guess_word + guessed_line[x+1:]
            x = x+1
    else:
        print("wrong guess")
    return guessed_line

    
def n_main():
    print ("Welcome.")
    s_word =(get_secret_word())
    guessed_line=(get_masked_word(s_word))
    print(get_masked_word(s_word))
    a =True    
    tries=10
    guess_word_list = []
    while a:
        print("tries left {}".format(tries))
        t_left = set_tries_left(tries)
        guess_word=input("input a char\n")
        if guess_word in guess_word_list:
            print("already guessed")
            continue
        else:
            guess_word_list.append(guess_word)
        guessed_line = type_guess_word(s_word, guess_word,guessed_line)
        print (guessed_line)
        print ("already guessed word{}".format(guess_word_list))
        tries = tries-1
        if (tries < 0):
            a= False
            print ("no tries left sorry..")
        
n_main()
