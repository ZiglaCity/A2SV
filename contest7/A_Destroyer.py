t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    mx = max(a)
    printed = False
    for i in range(mx, 0, - 1):
        # print(i, i - 1)
        # print(a.count(i), a.count(i - 1))
        if a.count(i) > a.count(i - 1):
            print("NO")
            printed = True
            break
    if not printed:
        print("YES")