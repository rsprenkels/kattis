from typing import Dict, Generator

def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n-1) + fib2(n-2)

def test_2():
    assert fib2(8) == 21



memo: Dict[int, int] = {0: 0, 1: 1}

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n-2)
    return memo[n]

def test_3():
    assert fib3(8) == 21

def test_3_big():
    assert fib3(50) == 12586269025

def test_3_reallybig():
    assert fib3(500) == 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125




def fib4(n: int) -> int:
    if n == 0: return n
    last: int = 0
    next: int = 1
    for _ in range(1,n):
        last, next = next, last + next
    return next

def test_4_big():
    assert fib4(50) == 12586269025





def fib6(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next

def test6():
    assert list(fib6(10)) == [0,1,1,2,3,5,8,13,21,34,55]
