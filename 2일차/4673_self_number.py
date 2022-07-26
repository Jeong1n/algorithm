num = set(range(1, 10001))
b = set()
for i in range(1, 10001):
    for c in str(i):
        i += int(c)
    b.add(i)

d = sorted(num - b)
for i in d:
    print(i)
    