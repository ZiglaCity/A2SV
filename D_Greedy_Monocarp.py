t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    
    ans = 0
    for i in range(n):
        if ans + a[i] > k:
            print(k - ans)
            ans += a[i]
            break
        if ans + a[i] == k:
            print(0)
            ans += a[i]
            break
        else:
            ans += a[i]
    if ans < k:
        print(k - ans)