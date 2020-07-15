import sys
import statistics

def monitor(line: str) -> str:
    tokens = line.split()
    name = []
    if tokens[0].isalpha():
        while tokens[0].isalpha():
            name.append(tokens.pop(0))
    else:
        while tokens[-1].isalpha():
            name.insert(0, tokens.pop())

    avg_heartrate = statistics.mean(list(map(float, tokens)))

    return f"{avg_heartrate} {' '.join(name)}"

def test_1():
    assert monitor('Lisa Marie Presley 90.2 104.3 110.1 118.7 122.3') == '109.120000 Lisa Marie Presley'

if __name__ == '__main__':
    for line in sys.stdin:
        print(monitor(line))

# from 396.0 rank 946 to 397.7 rank 941
