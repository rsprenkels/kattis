def parking(param) -> int:
    stores = list(map(int, param.split()))
    return (max(stores) - min(stores)) * 2

def test_1():
    assert parking('24 13 89 37') == 152

if __name__ == '__main__':
    num_cases = int(input())
    for case in range(num_cases):
        input()
        print(parking(input()))