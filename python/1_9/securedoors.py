from collections import defaultdict
from typing import Sequence


def secure_doors(events: Sequence[str]) -> Sequence[str]:
    state = defaultdict(bool)
    results = []
    for event in events:
        etype, who = event.split()
        if etype == 'entry':
            results.append(f'{who} entered{" (ANOMALY)" if state[who] else ""}')
            state[who] = True
        else:
            results.append(f'{who} exited{" (ANOMALY)" if not state[who] else ""}')
            state[who] = False
    return results

def test_1():
    events = """
entry Abbey
entry Abbey
exit Abbey
entry Tyrone
exit Mason
entry Demetra
exit Latonya
entry Idella
"""[1:-1].split('\n')

    expected_result = """
Abbey entered
Abbey entered (ANOMALY)
Abbey exited
Tyrone entered
Mason exited (ANOMALY)
Demetra entered
Latonya exited (ANOMALY)
Idella entered
"""[1:-1].split('\n')
    assert secure_doors(events) == expected_result

if __name__ == '__main__':
    events = []
    for _ in range(int(input())):
        events.append(input())
    print('\n'.join(secure_doors(events)))

# from 450.8 rank 806 to 452.7 rank 803