t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    if len(a) == 1:
        print(0)
    else:
        res = 0
        left = 0
        right = n - 1
        while left < right:
            res += (a[right] - a[left])
            left += 1
            right -= 1
        print(res)