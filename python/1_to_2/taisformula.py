from collections import namedtuple

num_samples = int(input())

datapoint = []

Measurement = namedtuple('Measurement', ['t','value'])
for sample_index in range(num_samples):
    datapoint.append(Measurement(*list(map(float, input().split()))))

running_total = 0.0
for dp_index in range(len(datapoint) - 1):
    m1, m2 = datapoint[dp_index:dp_index + 2]
    running_total += (m1.value + m2.value) / 2.0 * (m2.t - m1.t)

print(running_total / 1000.0)