from unittest.mock import patch


def spavanac():
    hour, minute = list(map(int, input().split()))
    minute -= 45
    if minute < 0:
        minute += 60
        hour -= 1
        if hour < 0:
            hour += 24
    print('{} {}'.format(hour, minute))


def test_spavanac(capsys):
    input = ['10 10']
    with patch('builtins.input', side_effect=input):
        spavanac()
    out, err = capsys.readouterr()
    assert out.split('\n')[:-1] == ['9 25']


if __name__ == '__main__':
    spavanac()
