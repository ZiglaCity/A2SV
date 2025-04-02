t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    res = ''
    sub = []
    for i, num in enumerate(p):
        s = set(range(1, num + 1))
        sub = p[0:i] if i - num <= 0 else p[i - num + 1: i]
        sub += p[i:-1] if i + num >= len(p) else p[i: i + num]
        print(s)
        print(sub)
        l = 0
        while l < len(sub):
            if sub[l] in s:
                count = 0
                while l < len(sub) and sub[l] in s:
                    count += 1
                    l += 1
                if count >= num:
                    res += '1'
                else:
                    res += '0'
                print(res)
                break
            l += 1
    print(res)