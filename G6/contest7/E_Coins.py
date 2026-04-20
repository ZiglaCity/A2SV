t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    printed = False
    for x in range(1, 100):
        if (n - k*(x)) % 2 == 0 or (n - 2*(x)) % k == 0:
            print("YES")
            printed = True
            break
    if not printed:
        print("NO")