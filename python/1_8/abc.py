def abc(numbers, letters):
    numbers.sort()
    output = [numbers[ord(letter) - ord('A')] for letter in letters]
    return output

assert abc([1,5,3], 'ABC') == [1,3,5]

numbers = list(map(int, input().split()))
letters = input()
print(' '.join(map(str, abc(numbers, letters))))

# from 369.3 rank 1029 to 371.1 rank 1023