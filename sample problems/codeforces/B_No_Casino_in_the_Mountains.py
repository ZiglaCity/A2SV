t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    total = count = 0
    rest = -1
    for i in range(n):
        if a[i] == 1:
            count = 0
        elif i > rest:
            count += 1
        if count == k:
            total += 1
            count = 0
            rest = i + 1
    print(total)