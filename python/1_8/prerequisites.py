from typing import Sequence, Tuple

def prereq(courses: Sequence[int], categories: Sequence[Tuple[int, Sequence[int]]]) -> bool:
    taken_in_category = [0] * len(categories)
    for course in courses:
        for ndx, category in enumerate(categories):
            if course in category[1]:
                taken_in_category[ndx] += 1
    for ndx, category in enumerate(categories):
        if taken_in_category[ndx] < category[0]:
            return False
    return True

def test_1():
    assert prereq([123, 9876, 2222], [(1, [8888, 2222]), (2, [9876, 2222, 7654])]) == True


def test_2():
    assert prereq([123, 9876, 2222], [(2, [8888, 2222]), (2, [9876, 2222, 7654])]) == False


if __name__ == '__main__':
    while True:
        line = input()
        if line == '0':
            break
        num_courses, num_categories = map(int, line.split())
        courses = list(map(int, input().split()))
        categories = []
        for c in range(num_categories):
            info = list(map(int, input().split()))
            categories.append((info[1], info[2:]))
        print(['no','yes'][prereq(courses, categories)])

# from 514.1 rank 683 (team 284.4 rank 132)