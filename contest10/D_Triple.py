t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    dic = {}
    printed = False
    for num in a:
        dic[num] = dic.get(num, 0) + 1
        if dic[num] >= 3:
            print(num)
            printed = True
            break
    
    if not printed:
        print(-1)