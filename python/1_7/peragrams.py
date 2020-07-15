from collections import defaultdict

def chars_to_peragram(word: str) -> int:
    letter_freq = defaultdict(int)
    for letter in word:
        letter_freq[letter] += 1
    need_removing = {k:v % 2 for k,v in letter_freq.items() if v % 2 == 1}
    if len(need_removing) == 0:
        return 0
    else:
        return len(need_removing) - 1

def test_pera1():
    assert chars_to_peragram('abc') == 2

def test_pera2():
    assert chars_to_peragram('aab') == 0

if __name__ == '__main__':
    print(chars_to_peragram(input()))

# from 399.4 rank 937 to 401.1 rank 931
