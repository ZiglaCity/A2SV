t = int(input())
for _ in range(t):
    n, c = input().split()
    n = int(n)
    s = input()

    if c == "g":
        print(0)
    else:
        mn = 0
        cur = s.index("g")
        for i in range(n - 1, -1, -1):
            if s[i] == "g":
                cur = i
            else:
                if s[i] == c:
                    if i > cur:
                        mn = max(mn, n - i + cur)
                    else:
                        mn = max(mn, cur - i)

        print(mn)
                