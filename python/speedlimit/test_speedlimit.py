from unittest.mock import patch


def speedtest():
    num_pairs: int = int(input())
    while num_pairs > 0:
        previous_time: int = 0
        distance: int = 0
        for pair_index in range(num_pairs):
            speed, time = list(map(int, input().split(" ")))
            distance += speed * (time - previous_time)
            previous_time = time
        print("{} miles".format(distance))
        num_pairs = int(input())


def test_speedtest(capsys):
    input = ['3', '20 2', '30 6', '10 7',
             '2', '60 1', '30 5',
             '-1']
    with patch('builtins.input', side_effect=input):
        speedtest()
    out, err = capsys.readouterr()
    assert out.split('\n')[:-1] == ['170 miles', '180 miles']


if __name__ == "__main__":
    speedtest()
