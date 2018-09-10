def hissingmicrophone(line: str) -> str:
    if line.find('ss') >= 0:
        return 'hiss'
    else:
        return 'no hiss'


def test_pos():
    assert hissingmicrophone("there is a hiss here") == "hiss"


def test_start():
    assert hissingmicrophone("ssthere is a nothing here") == "hiss"


if __name__ == '__main__':
    print(hissingmicrophone(input()))
