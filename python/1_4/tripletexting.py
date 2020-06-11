
def decode(message):
    word_list = []
    word_len = len(message) // 3
    for part in range(3):
        word_list.append(message[part * word_len:(part + 1) * word_len])
    result = []
    for index, letter in enumerate(word_list[0]):
        if letter == word_list[1][index]:
            result.append(letter)
        else:
            result.append(word_list[2][index])
    return ''.join(result)

assert decode('hejhejhej') == 'hej'

assert decode('hrllohellohello') == 'hello'

print(decode(input()))