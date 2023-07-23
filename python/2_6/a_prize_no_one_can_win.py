def solution(min_cost, prices):
    prices.sort()
    for ndx in range(len(prices) - 1):
        if sum(prices[ndx:ndx+2]) > min_cost:
            return ndx + 1
    return len(prices)

def test_1():
    assert solution(min_cost=6, prices=[1,2,3,4,5]) == 3

def test_2():
    assert solution(min_cost=10, prices=[1,3,1,7]) == 4

if __name__ == '__main__':
    num_prices, min_cost = list(map(int, input().split(' ')))
    prices = list(map(int, input().split(' ')))
    print(solution(min_cost=min_cost, prices=prices))