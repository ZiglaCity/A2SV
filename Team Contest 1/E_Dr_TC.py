t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ones = 0
    res = 0
    for num in s:
        if num == "1":
            ones += 1

    for num in s:
        if num == "0":
            res += ones + 1
        else:
            res += ones - 1
    print(res)
