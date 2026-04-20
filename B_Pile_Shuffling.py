t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    # we use the negative and pos to identify excess and needed
    # if we have excess zero, just move the excess as + (excesss)
    # if we have excess ones, we move we move all the zeros first and then move a one, i.e + (zeros on top + 1)
    res = 0
    for a, b, c, d in arr:
        res += (max(0, a - c))
        zeros_left = (a - c) if a > c else a
        res += (max(0, (zeros_left + b - d) if b - d > 0 else 0))
    print(res)