n, q = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
prefix = [0] * len(p)
prefix[0] = p[0]

for i in range(1, len(p)):
    prefix[i] = prefix[i - 1] + p[i]
for _ in range(q):
    x, y = map(int, input().split())
    result = prefix[n - x + y - 1] - (prefix[n - x - 1] if n - x - 1 >= 0 else 0)
    print(result)
 
