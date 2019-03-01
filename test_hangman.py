# test_hangman.py

import hangman

# 1. Secret word should have atleast 6 letters
# 2. Secret word should have no punctuation
# 3. Secret word should not be a proper noun

#   4. Masked secret word 
#   5. Number of tries left
#   6. Wrong guesses so far 

def test_secret_word_6_letters():
    assert all(hangman.get_secret_word("./test_data/1.words") == "policeman" for _ in range(100))

def test_secret_word_no_punctuation():
    assert all(hangman.get_secret_word("./test_data/2.words") == "fireman" for _ in range(100))

def test_secret_word_no_proper_nouns():
    assert all(hangman.get_secret_word("./test_data/3.words") == "policeman" for _ in range(100))

def test_guess_word_masked():
    assert (hangman.get_masked_word("policeman") == "*********")

def test_type_guess_word():
    assert (hangman.type_guess_word("policeman","a","*********") == "*******a*")
    assert (hangman.type_guess_word("policeman","p","*******a*") == "p******a*")
    assert (hangman.type_guess_word("policeman","q","p******a*") == "p******a*")

def test_user_input():
    def fake_input(_):
        return 'a'
    assert hangman.user_input(fake_input) == 'a'




