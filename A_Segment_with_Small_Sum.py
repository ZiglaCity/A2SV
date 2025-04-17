n, s = map(int, input().split())
arr = list(map(int, input().split()))
l = r = 0
res = 0
v = 0
while r < n:
    res += arr[r]
    while res > s:
        res -= arr[l]
        l += 1
    v = max(v, r - l + 1)
    r += 1
print(v)