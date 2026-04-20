n, k = map(int, input().split())
half = (n + 1) // 2
if k > half:
    print((k - half) * 2)
else:
    print((2 * k) - 1)