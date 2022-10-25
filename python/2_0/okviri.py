from typing import List

def solution(word: str) -> List[str]:
    result = [['.'] * (len(word) * 4 + 1) for _ in range(5)]
    for letter, ndx in zip(word, range(2, len(word)*4, 4)):
        result[2][ndx] = letter
    for ndx in range(len(word)):
        char = '#'
        if (ndx + 1) % 3 == 0:
            continue
        for row, dx in zip(range(5), [0,1,2,1,0]):
            result[row][ndx*4+2+dx] = char
            result[row][ndx*4+2-dx] = char
    for ndx in range(len(word)):
        char = '*'
        if (ndx + 1) % 3 != 0:
            continue
        for row, dx in zip(range(5), [0,1,2,1,0]):
            result[row][ndx*4+2+dx] = char
            result[row][ndx*4+2-dx] = char
    return [''.join(line) for line in result]

def test_1():
    assert solution('ABCD') == [
        '..#...#...*...#..',
        '.#.#.#.#.*.*.#.#.',
        '#.A.#.B.*.C.*.D.#',
        '.#.#.#.#.*.*.#.#.',
        '..#...#...*...#..',
        ]

if __name__ == '__main__':
    word = input()
    result = solution(word)
    print('\n'.join(result))
