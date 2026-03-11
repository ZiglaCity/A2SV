n, t = map(int, input().split())
a = list(map(int, input().split()))
l = r = res = 0
while r < n:
    t -= a[r]
    while t < 0:
        t += a[l]
        l += 1
    res = max(res, r - l + 1)
    r += 1
print(res)
