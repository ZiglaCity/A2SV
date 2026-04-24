n, d = map(int, input().split())
p = list(map(int, input().split()))

cur = res = 0
i = 0
p.sort(reverse=True)
while n > 0:
    cur = 0
    while n > 0 and cur <= d:
        cur += p[i]
        n -= 1
    i += 1
    if cur > d:
        res += 1

print(res)
