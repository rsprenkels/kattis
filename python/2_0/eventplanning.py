def solution(N, B, hotels) -> str:
    min_price = B + 1
    for h in hotels:
        price, rooms_available = h
        total_price = price * N
        has_room = max(rooms_available) >= N
        if total_price <= B and has_room:
            min_price = min(min_price, total_price)
    if min_price <= B:
        return str(min_price)
    else:
        return 'stay home'

def test_1():
    assert solution(3, 1000, [(200, [0,2,2]), (300,[27,3,20])]) == '900'

def test_2():
    assert solution(5, 2000, [(300, [4,3,0,4]), (450,[7,8,0,13])]) == 'stay home'

if __name__ == '__main__':
    N, B, H, W = list(map(int, input().split()))
    hotels = []
    for _ in range(H):
        price = int(input())
        rooms_available = list(map(int, input().split()))
        hotels.append((price, rooms_available))
    answer = solution(N, B, hotels)
    print(answer)