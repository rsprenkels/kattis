leaves_at, class_starts, num_rides = list(map(int, input().split()))

walk_times = list(map(int, input().split()))

ride_times = list(map(int, input().split()))

departure_times = list(map(int, input().split()))

cur_time = leaves_at + walk_times[0]

for ride in range(num_rides):
    wait_time = (departure_times[ride] - (cur_time % departure_times[ride])) % departure_times[ride]
    cur_time += wait_time + ride_times[ride] + walk_times[ride + 1]
    
if cur_time <= class_starts:
    print('yes')
else:
    print('no')
