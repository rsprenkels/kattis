def is_evenly_spaced(line: str) -> bool:
    dots = [len(p) for p in line[1:-1].split('*')]
    min_len = min(dots)
    max_len = max(dots)
    return min_len == max_len


def test_1():
    assert is_evenly_spaced('*.*.*.*.*.*.*.*.*') == True
    assert is_evenly_spaced('*..*.*.*.*.*.*.*.*') == False

def test_2():
    assert is_evenly_spaced('**********') == True



if __name__ == '__main__':
    case = 0
    while True:
        case += 1
        line = input()
        if line == 'END':
            break
        print(f'{case} ', end='')
        print(['NOT EVEN', 'EVEN'][is_evenly_spaced(line.strip())])

# from  511.6 rank 684 (team 283.5 rank 132)