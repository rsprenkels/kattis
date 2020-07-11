def candlebox(age_dif: int, rita: int, theo: int) -> int:
    candles_rita = list(range(4, 100))
    candles_theo = [0] * (age_dif - 1) + list(range(3, 100))
    for year in range(99):
        if sum(candles_rita[:year]) + sum(candles_theo[:year]) == rita + theo:
            return rita - sum(candles_rita[:year])

assert candlebox(2, 26, 8) == 4

age_dif = int(input())
rita_candles = int(input())
theo_candles = int(input())

print(candlebox(age_dif, rita_candles, theo_candles))

#from 372.9 rank 1019 to 375.5 rank 1013