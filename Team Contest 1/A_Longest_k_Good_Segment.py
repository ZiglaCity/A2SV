from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

counter = defaultdict(int)
set_k = set()
l = 0
mx = 1
res = [1, 1]

for r in range(n):
    counter[a[r]] += 1
    set_k.add(a[r])
    if len(set_k) <= k and r - l + 1 > mx:
        mx = r - l + 1
        res = [l + 1, r + 1]

    while len(set_k) > k:
        counter[a[l]] -= 1
        if counter[a[l]] == 0:
            set_k.remove(a[l])
        l += 1
print(*res)