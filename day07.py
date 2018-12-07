from collections import defaultdict

lines = open('07.txt').readlines()

m = defaultdict(set)
rm = defaultdict(set)

all_steps = set()

for line in lines:
    prior_step = line.split()[1]
    step = line.split()[7]
    all_steps.add(prior_step)
    all_steps.add(step)
    m[step].add(prior_step)
    rm[prior_step].add(step)


queue = sorted(all_steps - set(m.keys()), reverse=True)
visited = []

while queue:
    x = queue.pop()
    if x not in visited:
        if not m[x] - set(visited):
            visited.append(x)
            queue += rm[x]
            queue = sorted(set(queue), reverse=True)
        else:
            queue.insert(0, x)

# part 1
print(''.join(visited))


total_time = 0
queue = sorted(all_steps - set([y for y in m.keys() if len(m[y]) > 0]), reverse=True)
visited = []


# max = 5
inflights = {}
no_new_work = 0
while queue or inflights:
    if len(inflights) < 5 and queue and no_new_work < len(queue):
        x = queue.pop()
        if x not in visited:
            if not m[x] - set(visited):
                no_new_work = 0
                inflights[x] = 61 + (ord(x) - ord('A'))
            else:
                no_new_work += 1
                queue.insert(0, x)
    else:
        min_time = min(inflights.values())
        total_time += min_time
        done_candidates = []
        for k, v in inflights.items():
            inflights[k] = v - min_time
            if inflights[k] == 0:
                done_candidates.append(k)
        for k in sorted(done_candidates):
            visited.append(k)
            queue += rm[k]
            queue = sorted(set(queue), reverse=True)
            no_new_work = 0
            del inflights[k]

# part 2
print(total_time)
