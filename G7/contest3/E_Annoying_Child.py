t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    evens = [v for v in a if v % 2 == 0]
    odds = [v for v in a if v % 2]

    if evens and not odds:
        print(*([0] * n))
        continue

    if odds and not evens:
        mx = odds[0]
        print(*[mx if k % 2 == 1 else 0 for k in range(1, n + 1)])
        continue

    res = []

    for i in range(1, len(evens)):
        evens[i] += evens[i - 1]

    maxOdd = odds[0]
    sumEven = evens[-1]
    minEven = a[-1] if a[-1] % 2 == 0 else min(v for v in a if v % 2 == 0)

    for k in range(1, n + 1):

        if k == 1:
            res.append(maxOdd)

        elif k <= len(evens) + 1:
            res.append(maxOdd + evens[k - 2])

        else:
            extra = k - (len(evens) + 1)

            if extra % 2 == 0:
                res.append(maxOdd + sumEven)
            else:
                if k == n:
                    res.append(0)
                else:
                    res.append(maxOdd + sumEven - minEven)

    print(*res)