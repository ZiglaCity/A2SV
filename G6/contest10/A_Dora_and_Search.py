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
        
        


# def check(a, n):
#     l, r = 0, n - 1
#     mn, mx = 1, n
    
#     while l <= r:
#         if mx not in (a[l], a[r]) and mn not in (a[l], a[r]):
#             print(l + 1, r + 1)
#             return
        
#         if mn in (a[l], a[r]):
#             if a[l] == mn:
#                 l += 1
#             else:
#                 r -= 1
#             mn += 1

#         if l < n and r >= 0 and mx in (a[l], a[r]):
#             if a[r] == mx:
#                 r -= 1
#             else:
#                 l += 1
#             mx -= 1
    
#     print(-1)

# t = int(input().strip())
# for _ in range(t):
#     n = int(input().strip())
#     a = list(map(int, input().split()))
    
#     perm = list(range(1, n + 1))
#     if sorted(a) != perm or perm == a:
#         print(-1)
#         continue
#     check(a, n)


