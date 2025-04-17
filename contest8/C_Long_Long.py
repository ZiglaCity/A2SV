t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    right = 0
    mx = 0
    count = 0
    while right < n:
        if a[right] < 0:
            count +=1
            while right < n and a[right] <= 0:
                mx += (-a[right])
                right += 1
        else:
            mx += a[right]
            right += 1
    print(mx, count)
        
