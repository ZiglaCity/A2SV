t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    prefix = [0] * n
    suffix = [0] * n
    res = []

    prefix[0] = a[0]
    for i in range(1, n):
        prefix[i] = min(prefix[i - 1], a[i])

    suffix[-1] = a[-1]
    for i in range(n - 2, -1, -1):
        suffix[i] = max(suffix[i + 1], a[i])

    for i in range(n):
        res.append("1" if a[i] == prefix[i] or a[i] == suffix[i] else "0")

    print("".join(res))
