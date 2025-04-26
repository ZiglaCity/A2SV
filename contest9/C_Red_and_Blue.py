t = int(input())
for _ in range(t):
    n = int(input()) - 1
    r = list(map(int, input().split()))
    m = int(input()) - 1
    b = list(map(int, input().split()))
    
    max_r = 0
    res = 0
    for num in r:
        res += num
        max_r = max(max_r, res )
    
    max_b = 0
    res = 0
    for num in b:
        res += num
        max_b = max(max_b, res)
    
    print(max(0, max_r, max_b, max_r + max_b))
    # i = j = 0
    # res = []
    # while i < m and j < n:
    #     if r[j] > b[i]:
    #         res.append(r[j])
    #         j += 1
    #     else:
    #         res.append(b[i])
    #         i += 1
    # res += r[j:] + b[i:]
    # total = 0
    # mx = 0
    # for num in res:
    #     total += num
    #     mx = max(mx, total)

    # print(mx)
