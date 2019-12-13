def deathknight(param):
    return 'CD' not in param


def test_1():
    assert deathknight('DCOOO') == True


def test_2():
    assert deathknight('DODOCD') == False


if __name__ == '__main__':
    lines = [input() for _ in range(int(input()))]
    print(sum([1 for line in lines if deathknight(line)]))
