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

    
def set_masked_letter():
    print ("Welcome.")
    s_word =(get_secret_word())
    guessed_line=(get_masked_word(s_word))
    print(get_masked_word(s_word)) 
    tries=10
    guesses =[]
    
    while True:
        t_left = set_tries_left(tries)
        guess_word=input("input a char\n")
       
        print(type_guess_word(s_word, guess_word,guessed_line))
        if guess_word in s_word:
            print(guessed_line)
            g=guesses.append(guess_word)
        else:
            tries = tries-1
        print("You have only {} tries left\n".format(tries))
        print("Already guessed letters",guesses,"\n")    
        if (tries == 0):
            print (f"Sorry you lost the game,no tries left. the word is:{s_word}")
            break

def won_game():
    m_left=set_masked_letter()
    
    if tries > 0:
        print("Congrats...you won the game")
    else:
        print("sorry you lost")
        
        
        

set_masked_letter()
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


    
def set_masked_letter():
    print ("Welcome.")
    s_word =(get_secret_word())
    guessed_line=(get_masked_word(s_word))
 
    tries=10
    guesses =[]
    g_line=[]
    while True:
        print(get_masked_word(guessed_line)) 
       # t_left = set_tries_left(tries)
        guess_word=input("input a char\n")
        guesses.append(guess_word)
        if guess_word in guesses:
            print("aready guess")
        else:
            print(type_guess_word(s_word, guess_word,guessed_line))
        if guess_word in s_word:
            print(guessed_line)
        else:
            tries = tries-1
        print("You have only {} tries left".format(tries))
        print("Already guessed letters",g_line,)
        if (tries == 0):
            print (f"Sorry you lost the game,no tries left. the word is:{s_word}")
            break
        if (tries >=1):
            print("you won")
            break

def won_game():
    m_left=set_masked_letter()
    
    if tries > 0:
        print("Congrats...you won the game")
    else:
        print("sorry you lost")


if __name__ == __"main"__:
    set_masked_letter()


