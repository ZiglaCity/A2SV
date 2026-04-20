t = int(input())
for _ in  range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    printed = False
    for i in range(n - 1):
        if arr[i] <= arr[i + 1]:
            print("YES")
            printed = True
            break
    if not printed:
        print("NO")
    
    # e = (n * (n - 1) // 2) - 1
    # j = 0
    # count = 0
    # broken = False
    # for i in range(n):
    #     swapped = False
    #     if count >= e:
    #         broken = True
    #         break
    #     for j in range(n - i - 1):
    #         if count >= e:
    #             broken = True
    #             break
    #         if arr[j] > arr[j + 1]:
    #             arr[j], arr[j + 1] = arr[j + 1], arr[j]
    #             count += 1
    #             swapped = True
    #     if not swapped or broken:
    #         break
    
    # if count >= e:
    #     print("NO")
    # else:
    #     print("YES")