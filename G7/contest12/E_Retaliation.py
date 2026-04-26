t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    can = True
    diff = a[1] - a[0]
    for i in range(2, n):
        if a[i] - a[i - 1] != diff:
            # print("here")
            print("NO")
            break
    else:
        num = n * a[0] - a[-1]
        den = n * n - 1
        # print(num, den)
        if num % den != 0:
            print("NO")
            continue
            
        y = num // den
        x = a[0] - n * y
  
        if x < 0 or y < 0:
            print("NO")
            continue

        print("YES")
        # for i in range(1, n):
        #     if abs(a[i] - a[i - 1]) > 2 * (min(a[i], a[i - 1])):
        #         print("NO")
        #         break
        # else:
        #     print("YES")
