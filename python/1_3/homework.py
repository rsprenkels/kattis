# https://open.kattis.com/problems/heimavinna

def solution(problems: str) -> int:
    total = 0
    for part in problems.split(';'):
        # print(f'found part {part}')
        if part.find('-') != -1:
            # print(f'getting ranges from {part}')
            prob_from, prob_to = list(map(int, part.split('-')))
            total += prob_to - prob_from + 1
        else:
            total += 1
    return total

def test_1():
    assert solution('3-10') == 8

def test_2():
    assert solution('1;3;5;8;13') == 5

if __name__ == '__main__':
    problems = input()
    result = solution(problems)
    print(result)
