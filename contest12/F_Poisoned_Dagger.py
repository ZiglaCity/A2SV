t = int(input())
for _ in range(t):
    n , h = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort(reverse=True)
    dif = []
    for i in range(n - 1):
        dif.append(a[i] - a[i + 1])

    def is_enough(k):
        total = 0
        for d in dif:
            total += min(k, d)
        total += k 
        return total >= h

    left, right = 1, h
    while left < right:
        mid = (left + right) // 2
        if is_enough(mid):
            right = mid
        else:
            left = mid + 1
    print(right)