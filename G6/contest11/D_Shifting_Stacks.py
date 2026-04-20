t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    res = 0
    possible = True
    for i in range(n):
        res += arr[i]
        if res < (i * (i + 1)) // 2:
            possible = False
            break
    print("YES" if possible else "NO")

    # res = sum(arr)
    # if n == 1:
    #     print("YES")
    # else:
    #     perm = (n * (n - 1)) / 2
    #     if  res < perm:
    #             print("NO")
    #     else:
    #         print("YES")

