import fileinput


def relocation(param):
    N, Q = list(map(int, param.pop(0).split()))
    locations = list(map(int, param.pop(0).split()))
    output = []
    for rq in range(Q):
        req_type, a, b = list(map(int, param.pop(0).split()))
        if req_type == 1: # move
            locations[a - 1] = b
        else: # dist_request
            output.append(f"{abs(locations[a - 1] - locations[b - 1])}")
    return '\n'.join(output)

def test_relocation():
    sample_input = """5 10
5 2 8 1 4
1 2 10
2 4 5
2 1 3
1 4 3
2 1 5
2 5 2
1 4 1
2 2 4
1 3 15
2 4 1"""
    sample_output = """3
3
1
6
9
4"""
    
    assert relocation(sample_input.split('\n')) == sample_output

if __name__ == '__main__':
    lines = []
    for line in fileinput.input():
        lines.append(line)
    print(relocation(lines))