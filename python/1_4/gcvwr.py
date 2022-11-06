def solution(G: int, T: int, tot_items: int) -> int:
    return int(((G - T) * 0.9) - tot_items)

def test_1():
    assert solution(12000, 3000, sum([400, 25, 200, 80, 500])) == 6895

if __name__ == '__main__' :
    G,T,N = list(map(int, input().split()))
    tot_items = sum(map(int, input().split()))
    print(solution(G, T, tot_items))


# 12000 3000 5
# 400 25 200 80 500
# 6895