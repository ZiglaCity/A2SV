t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print("NO" if min(m, n) == 1 else "YES") 