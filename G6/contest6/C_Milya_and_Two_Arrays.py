t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    set_a = set(a)
    set_b = set(b)
    c = set()
    for element1 in set_a:
        for element2 in set_b:
            c.add(element1 + element2)
    print("YES"  if len(c) >= 3 else "NO")
    # if len(set_a) > 2 or len(set_b) > 1:
    #     print("YES")
    #     continue

    # elif len(set_a) == 2:
    #     if len(set_b) == 1:
    #         print("NO")
    #         continue
    #     else:
    #         print("YES")
    #         continue

    # elif len(set_b) == 2:
    #     if len(set_a) == 1:
    #         print("NO")
    #         continue
    #     else:
    #         print("YES")
    #         continue
    # elif len(set_b) == 1 and len(set_a) == 1:
    #     print("NO")
    #     continue
    # else:
    #     print("YES")
    #     continue