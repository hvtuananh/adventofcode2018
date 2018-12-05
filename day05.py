input_text = open('05.txt').read().strip()

cache = set()
for c in input_text:
    cache.add(c.lower())


def colapse(text, ignore=None):
    stack = []

    for c in text:
        if ignore and c.lower() == ignore:
            continue
        if not stack:
            stack.append(c)
        elif c != stack[-1] and c.lower() == stack[-1].lower():
            stack.pop()
        else:
            stack.append(c)

    return stack

# part 1
print(len(colapse(input_text)))

# part 2
print(min([len(colapse(input_text, cc)) for cc in cache]))
