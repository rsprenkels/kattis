def shiftback(letter: str, amount: str) -> str:
    amount_int = ord(amount) - ord('A')
    return chr(ord('A') + (ord(letter) - ord('A') - amount_int + 26) % 26)

def decrypt(cipher : str, secret : str) -> str:
    message = []
    key = [c for c in secret]
    for i in range(len(cipher)):
        message.append(shiftback(cipher[i], key[i]))
        key.append(message[-1])
    return ''.join(message)

assert decrypt(cipher='SGZVQBUQAFRWSLC', secret='ACM') == 'SENDMOREMONKEYS'

print(decrypt(input(), input()))

# from 380.7 rank 985 to 382.4 978
