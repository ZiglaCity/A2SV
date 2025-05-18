n, t = map(int, input().split())
a = list(map(int, input().split()))

count = total = l = 0

for r in range(n):
    total += a[r]
    while total > t:
        total -= a[l]
        l += 1
    count = max(count, r - l + 1)

print(count)