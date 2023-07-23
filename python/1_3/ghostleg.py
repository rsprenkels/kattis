def solution(num_elements, rungs):
    elements = list(range(1, num_elements+1))
    for rung in rungs:
        ndx = rung - 1
        elements[ndx], elements[ndx+1] = elements[ndx+1],elements[ndx]
    return elements

def test_1():
    assert solution(4, [1,2,1,3,2]) == [3,4,2,1]

if __name__ == '__main__':
    num_elements, num_rungs = list(map(int, input().split(' ')))
    rungs = []
    for _ in range(num_rungs):
        rungs.append(int(input()))
    print('\n'.join(map(str, solution(num_elements, rungs))))