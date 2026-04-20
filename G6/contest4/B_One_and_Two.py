n = int(input())
for _ in range(n):
    t = int(input())
    a = list(map(int, input().split()))
    total = 1
    k = 0
    for num in a:
        total *= num
    i = 1
    cur = a[0]
    while i < t:
        if total/cur == cur:
            k = i
            break
        cur *= a[i]
        i += 1
    print(k if k != 0 else -1)
