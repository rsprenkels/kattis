num_testcases = int(input())

for testcase in range(num_testcases):
    print(f"running testcase {testcase}")

    visited_cities = set()
    num_trips = int(input())
    for tip in range(num_trips):
        visited_cities.add(input())
    print(len(visited_cities))
