def toggle_case(p):
    res = []
    for c in p:
        if c.isalpha():
            if c.isupper():
                res.append(c.lower())
            else:
                res.append(c.upper())
        else:
            res.append(c)
    return ''.join(res)

def softpasswords(s: str, p: str) -> bool:
    if s == p:
        return True
    if s[:-1] == p and s[-1:].isdecimal():
        return True
    if s[1:] == p and s[:1].isdecimal():
        return True
    if s == toggle_case(p):
        return True
    return False


def test_1():
    assert softpasswords('123', '123a') == False


def test_2():
    assert softpasswords('abc', 'ABC') == True


def test_3():
    assert softpasswords('c0deninja5', 'c0deninja') == True


def test_4():
    assert softpasswords('sk5B35HJ', 'sk5B35HJ') == True

if __name__ == '__main__':
    if softpasswords(input(), input()):
        print('Yes')
    else:
        print('No')

# from 500.0 rank 708

