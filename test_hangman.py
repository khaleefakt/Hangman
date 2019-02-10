# test_hangman.py

import hangman

# 1. Secret word should have atleast 6 letters
# 2. Secret word should have no punctuation
# 3. Secret word should not be a proper noun

#   1. Masked secret word (* for unguessed letters, actual letter for correctly guessed letters)
#   2. Number of tries left (start with 10)
#   3. Wrong guesses so far 

def test_secret_word_6_letters():
    assert all(hangman.get_secret_word("./test_data/1.words") == "policeman" for _ in range(100))

def test_secret_word_no_punctuation():
    assert all(hangman.get_secret_word("./test_data/2.words") == "fireman" for _ in range(100))

def test_secret_word_no_proper_nouns():
    assert all(hangman.get_secret_word("./test_data/3.words") == "policeman" for _ in range(100))

def test_guess_word_masked():
    assert (hangman.get_guess_word("/usr/share/dict/words") == "*********" for _ in range(100))

def test_tries_left():
    assert (hangman.set_tries_left() == "tries" for _ in range(100))

    
