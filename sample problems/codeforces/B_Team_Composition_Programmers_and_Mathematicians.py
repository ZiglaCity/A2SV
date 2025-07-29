t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    res = min((a + b) // 4, a, b)
    print(res)

# t = int(input())
# for _ in range(t):
#     a, b = map(int, input().split())
#     res = 0
#     mn = min(a, b)
#     mx = max(a, b)
#     if mx >= (mn * 3):
#         res = mn
#     else:
#         res = (mn + mx) // 4
#     print(res)

