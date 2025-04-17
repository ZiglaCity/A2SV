t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    left = 0
    right = n - 1
    res  = []
    while left < right:
        res.append(b[left])
        res.append(b[right])
        left += 1
        right -= 1
    if n % 2 == 1:
        res.append(b[left])
    print(*res)