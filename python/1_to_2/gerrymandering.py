from collections import namedtuple
from collections import defaultdict

# https://open.kattis.com/problems/gerrymandering

Votes = namedtuple('Votes',['A','B'], defaults=(0,) * 2)

def gerry(p, d, results):
    district_results = defaultdict(Votes)
    for result in results:
        district, A, B = list(map(int, result.split()))
        was = district_results[district]
        district_results[district] = Votes(was.A + A, was.B + B)
    output = []
    total_votes = Votes()
    total_wasted = Votes()
    for d in [district_results[d] for d in sorted(district_results.keys())]:
        total_votes = Votes(total_votes.A + d.A, total_votes.B + d.B)
        if d.A > d.B:
            wasted_a = d.A - ((d.A + d.B) // 2 + 1)
            wasted_b = d.B
            output.append(f"A {wasted_a} {wasted_b}\n")
        else:
            wasted_a = d.A
            wasted_b = d.B - ((d.A + d.B) // 2 + 1)
            output.append(f"B {wasted_a} {wasted_b}\n")

        total_wasted = Votes(total_wasted.A + wasted_a, total_wasted.B + wasted_b)

    output.append(f"{abs(total_wasted.A - total_wasted.B) / (total_votes.A + total_votes.B):.10}")
    return ''.join(output)


def test_gm():
    p, d = (5,3)
    results = """\
1 100 200
2 100 99
3 100 50
3 100 50
2 100 98
"""
    assert gerry(p,d,results.split('\n')[:-1]) == """\
B 100 49
A 1 197
A 49 100
0.1965897693"""

if __name__ == '__main__':
    p,d = list(map(int, input().split()))
    results = []
    for r in range(p):
        results.append(input())
    print(gerry(p,d, results))