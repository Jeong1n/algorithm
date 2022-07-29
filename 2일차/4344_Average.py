a = int(input())

for i in range(a):
    c = list(map(int, input().split()))
    avg = sum(c[1:])/c[0]
    cnt = 0
    for score in c[1:]:
        if score > avg:
            cnt += 1
    rate = cnt/c[0]* 100
    print(f'{rate:.3f}%')