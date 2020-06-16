def rotate(c, amount):
    return chr(ord('A') + (26 + (ord(c) - ord('A')) + amount) % 26)

def decrypt(cipher_text, key):
    plain_text = []
    for ndx, c in enumerate(cipher_text):
        amount = ord(key[ndx]) - ord('A')
        if ndx % 2 == 0: # decrypt, so even is shift back, odd is forward
            amount = -amount
        plain_text.append(rotate(c, amount))
    return ''.join(plain_text)

assert decrypt(cipher_text='CPMCRYY', key='ALBERTA') == 'CALGARY'

assert decrypt(cipher_text='TDLIVA', key='OILERS') == 'FLAMES'

print(decrypt(cipher_text=input(), key=input()))
