import math

def kattis_score(points_list):
    return (1 / 5) * sum([p * math.pow(4 / 5, ind) for ind, p in enumerate(points_list)])


def reduced_score(point_list):
    orig_score = kattis_score(point_list)    

    total = 0.0
    for leave_out in range(len(point_list)):
        sublist = [p for ind, p in enumerate(point_list) if ind != leave_out]
        total += kattis_score(sublist)
    reduced = total / len(point_list)
    
    return orig_score, reduced


list_1 = [500, 120, 75]

assert kattis_score(list_1) == 128.8
assert reduced_score(list_1) == (128.8, 89.06666666666666)

assert reduced_score([100, 100]) == (36.0, 20.0)

team_points = []
list_len = int(input())
for _ in range(list_len):
    team_points.append(int(input()))
    
print('\n'.join(map(str, reduced_score(team_points))))
