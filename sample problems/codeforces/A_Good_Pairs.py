t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    mx = max(a)
    mn = min(a)
    print(a.index(mn) + 1, a.index(mx) + 1)



# apparently this approach is relatively slow, so let's try to optimize it
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     def check(n):
#         for i in range(n):
#             for j in range(n):
#                 stopped = False
#                 for k in range(n):
#                     if abs(a[i] - a[k]) + abs(a[k] - a[j]) != abs(a[i] - a[j]):
#                         stopped = True
#                         break
#                 if not stopped:
#                     return i + 1, j + 1

#     print(*check(n))