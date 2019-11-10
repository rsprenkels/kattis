def tri(a, b, c):
    if a + b == c:
        return f"{a}+{b}={c}"
    elif a - b == c:
        return f"{a}-{b}={c}"
    elif a // b == c:
        return f"{a}/{b}={c}"
    elif a * b == c:
        return f"{a}*{b}={c}"
    elif a == b + c:
        return f"{a}={b}+{c}"
    elif a == b - c:
        return f"{a}={b}-{c}"
    elif a == b // c:
        return f"{a}={b}/{c}"
    elif a == b * c:
        return f"{a}={b}*{c}"


def test_1():
    assert tri(5,3,8) == '5+3=8'

if __name__ == '__main__':
    print(tri(*list(map(int, input().split()))))