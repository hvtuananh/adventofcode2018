total = 0
inputs = map(int, open('08.txt').read().split())
i = 0
current_node = 0
graph = {}
stack = []
while i < len(inputs):
    # firs two is child + metadata
    child, metadata = inputs[i], inputs[i + 1]
    if child == 0:
        value = sum(inputs[i + 2:i + 2 + metadata])
        total += value
        i += 2 + metadata
        while stack:
            if stack[-1][0] == 1:
                x, y, z = stack.pop()
                total += sum(inputs[i:i + y])
                z.append(value)
                value = sum(z[j - 1] for j in inputs[i:i + y] if j <= len(z))
                i += y
            else:
                stack[-1][2].append(value)
                stack[-1] = (stack[-1][0] - 1, stack[-1][1], stack[-1][2])
                break
    else:
        # use stack
        stack.append((child, metadata, []))
        i += 2

# part 1
print(total)


# part 2
print(value)
