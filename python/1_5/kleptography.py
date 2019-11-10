# https://open.kattis.com/problems/kleptography

def kleptography(key_len, message_len, last_plaintext, ciphertext):
    key = []
    plain_text = last_plaintext
    for index in range(message_len - key_len):
        res = (ord(ciphertext[-1 - index]) - ord(plain_text[-1 - index]) + 26) % 26
        plain_text = chr(res + ord('a')) + plain_text
    return plain_text


def test_kleptography():
    assert kleptography(1, 12, 'd', 'fzvfkdocukfu') == 'shortkeyword'

def test_2():
    assert kleptography(5, 16, 'again', 'pirpumsemoystoal') == 'marywasnosyagain'

if __name__ == '__main__':
    key_len, message_len = list(map(int, input().split()))
    last_plaintext = input()
    ciphertext = input()
    print(kleptography(key_len, message_len, last_plaintext, ciphertext))