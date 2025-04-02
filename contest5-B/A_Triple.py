t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    dic = {}
    res = -1
    for num in arr:
        dic[num] = dic.get(num, 0) + 1
        if dic[num] >= 3:
            res = num
            break
    print(res)