n = int(input().strip())
v = list(map(int, input().split()))
m = int(input().strip())

prefix_v = [0] * (n + 1)
prefix_sorted_v = [0] * (n + 1)

sorted_v = sorted(v)

for i in range(1, n + 1):
    prefix_v[i] = prefix_v[i - 1] + v[i - 1]
    prefix_sorted_v[i] = prefix_sorted_v[i - 1] + sorted_v[i - 1]

for _ in range(m):
    typ, l, r = map(int, input().split())
    
    if typ == 1:
        print(prefix_v[r] - prefix_v[l - 1])
    else:
        print(prefix_sorted_v[r] - prefix_sorted_v[l - 1])
