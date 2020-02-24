from typing import List

def missing_numbers(num_list: List[int]):
    missing = [n for n in list(range(1, num_list[-1])) if n not in num_list]
    if not missing:
        print('good job')
    else:
        for m in missing:
            print(m)

if __name__ == '__main__':
    num_recited = int(input())
    recited = []
    for _ in range(num_recited):
        recited.append(int(input()))
    missing_numbers(recited)