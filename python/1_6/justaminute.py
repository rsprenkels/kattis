# https://open.kattis.com/problems/justaminute

def justaminute(measurements):
    cum_minutes = 0
    cum_seconds = 0
    for measurement in measurements:
        minutes, seconds = measurement
        cum_minutes += minutes
        cum_seconds += seconds
    factor =  cum_seconds / (60.0 * cum_minutes)
    if factor <= 1.0:
        return (False, "measurement error")
    else:
        return (True, factor)


def test_1():
    res = justaminute([(1, 61)])
    assert res[0] == True
    assert abs(res[1] - 1.016666667) < 0.0000001


def test_2():
    res = justaminute([(5, 560), (10, 600), (2, 264)])
    assert res[0] == True
    assert abs(res[1] - 1.396078431) < 0.0000001

if __name__ == '__main__':
    num_observations = int(input())
    measurements = []
    for _ in range(num_observations):
        measurements.append(tuple(list(map(int, input().split()))))
    result = justaminute(measurements)
    if result[0]:
        print(result[1])
    else:
        print(result[1])