# https://open.kattis.com/problems/prva

def prva(puzzle):
    words = set()
    for row in puzzle:
        words.update(row.split('#'))
    for col in range(len(puzzle[0])):
        totcol = ''.join([puzzle[r][col] for r in range(len(puzzle))])
        words.update(totcol.split('#'))
    return sorted([word for word in words if len(word) >= 2])[0]


def test_1():
    puzzle = [
        'luka',
        'o#a#',
        'kula',
        'i#a#', ]
    assert prva(puzzle) == 'kala'


def test_2():
    puzzle = [
        'luka',
        'o#a#',
        'kula',
        'i#as', ]
    assert prva(puzzle) == 'as'


if __name__ == '__main__':
    rows, cols = map(int, input().split())
    puzzle = []
    for _ in range(rows):
        puzzle.append(input())
    print(prva(puzzle))
