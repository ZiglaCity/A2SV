t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    l, r = 0 , len(a) - 1
    mn = 1
    mx = n
    found = False
    while r - l >= 3:
        if a[l] == mn:
            l += 1
            mn += 1
        elif a[l] == mx:
            l += 1
            mx -= 1
        elif a[r] == mn:
            r -= 1
            mn += 1
        elif a[r] == mx:
            r -= 1
            mx -= 1
        else:
            print(l + 1, r + 1)
            found = True
            break

    if not found:
        print(-1)
        
        