t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(0)
        continue

    res = []
    if (a[0] + a[-1]) % 2:
        cur = a[0]
    else:
        cur = a[-1]
    res.append((1, n))
    
    for i in range(1, n - 1):
        if (a[i] + cur) % 2:
            res.append((1, i + 1))
        else:
            res.append((i + 1, n))
    
    print(len(res))
    for r in res:
        print(*r)
    