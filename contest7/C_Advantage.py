t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    mx = max(a)
    next_max = sorted(a)[-2]
    res = []
    for num in a:
        if num == mx:
            res.append(num - next_max) 
        else:
            res.append(num - mx)
    print(*res)