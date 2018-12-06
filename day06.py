import sys
import numpy as np
from collections import defaultdict


input_text = map(str.strip, open('06.txt').readlines())

cache = {}
for i, line in enumerate(input_text):
    cache[i + 1] = map(int, line.split(','))


def find_min_point_and_distance(x, y):
    min_dist = sys.maxint
    distance = 0
    min_i = []
    for i, coords in cache.items():
        distance += abs(x - coords[0]) + abs(y - coords[1])
        if min_dist > abs(x - coords[0]) + abs(y - coords[1]):
            min_dist = abs(x - coords[0]) + abs(y - coords[1])
            min_i = [i]
        elif min_dist == abs(x - coords[0]) + abs(y - coords[1]):
            min_i.append(i)
    if len(min_i) == 1:
        return min_i[0], distance
    else:
        return -1, distance


max_x = max(x[0] for x in cache.values()) + 1
max_y = max(x[1] for x in cache.values()) + 1

m = np.zeros((max_x, max_y))
mmm = np.zeros((max_x, max_y))
for x in range(max_x):
    for y in range(max_y):
        m[x, y], mmm[x, y] = find_min_point_and_distance(x, y)


infinites = set(list(m[0, :]) + list(m[-1, :]) + list(m[:, 0]) + list(m[:, -1]))

total = defaultdict(int)
for x in range(max_x):
    for y in range(max_y):
        if m[x, y] not in infinites:
            total[m[x, y]] += 1

# part 1
print(max(total.values()))

# part 2
print((mmm < 10000).sum())
