t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    # if there's a single 0 in between 2 ones its impossible
    printed = False
    for i in range(1, len(b)):
        if b[i] == 0:
            if b[i - 1] == 1 and i + 1 < len(b) and  b[i + 1] == 1:
                print("NO")
                printed = True
                break
    
    if not printed:
        print("YES")

    # zero = 0
    # one = 0
    # printed = False
    # for i in range(len(b)):
    #     if b[i] == 0:
    #         zero += 1
    #         if one == 2 and (i != len(b) - 1 or i != 0):
    #             print("NO")
    #             printed = True
    #             break
    #         one = 0
    #     else:
    #         one += 1
    #         if zero == 2 and (i != len(b) - 1 or i != 0):
    #             print("NO")
    #             printed = True
    #             break
    #         zero = 0

    # if not printed:
    #     print("YES")