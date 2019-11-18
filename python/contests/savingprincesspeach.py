# https://open.kattis.com/contests/hsc8sj/problems/princesspeach

def princesspeach(total_obstacles, seen_obstacles):
    missed_list = [ob for ob in range(total_obstacles) if ob not in seen_obstacles]
    return (missed_list, total_obstacles - len(missed_list))


def test_1():
    assert princesspeach(20, [5, 10, 12, 16]) == (
        [0, 1, 2, 3, 4, 6, 7, 8, 9, 11, 13, 14, 15, 17, 18, 19],
        4)


if __name__ == '__main__':
    total_obstacles, num_seen = list(map(int, input().split()))
    seen_obstacles = []
    for _ in range(num_seen):
        seen_obstacles.append(int(input()))
    missed_list, got_this_many = princesspeach(total_obstacles, seen_obstacles)
    for missed in missed_list:
        print(missed)
    print(f"Mario got {got_this_many} of the dangerous obstacles.")
