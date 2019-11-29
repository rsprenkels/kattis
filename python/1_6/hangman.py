# https://open.kattis.com/problems/hangman

def hangman(word, guesses):
    word_letters = {letter for letter in word}
    wrong_guesses = 0
    for guess in guesses:
        if not guess in word:
            wrong_guesses += 1
            if wrong_guesses == 10:
                return 'LOSE'
        else:
            word_letters.remove(guess)
            if len(word_letters) == 0:
                return 'WIN'
    return 'SHOULD_NEVER_OCCUR'


def test_1():
    assert hangman('HANGMAN', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'WIN'


def test_2():
    assert hangman('BANANA', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'LOSE'


if __name__ == '__main__':
    word = input()
    guesses = input()
    print(hangman(word, guesses))
