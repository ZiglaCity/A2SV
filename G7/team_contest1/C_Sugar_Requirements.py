t = int(input())
import bisect 
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    
    for i in range(1, n):
        a[i] += a[i - 1]

    for _ in range(q):
        x = int(input())
        cur = bisect.bisect_left(a, x)

        print(-1 if cur == n else cur + 1)
