t = int(input())
for _ in range(t):
    n = int(input())
    w = list(map(int, input().split()))
    prefix = [w[0]]
    postfix = [w[-1]]
    # we loop through the prefix if the sum at any point is seen in the postfix
    # then that point can be a valid point
    # hence we calculate the total there
    for i in range( n - 2, -1, -1):
        postfix.append(postfix[-1] + w[i])
    
    # print(prefix, postfix)

    res =0 
    j = 0
    mx = 0
    for i in range(n):
        res += w[i]
        while res > postfix[j]:
            j += 1
        if res == postfix[j] and i + j + 1 < n:
            mx = max(mx, i + j + 2)

    print(mx)