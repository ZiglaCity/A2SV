n = int(input())
for _ in range(n):
    a, b, c, d = map(int, input().split())
    # if the difference between the two is greater than 6 check the the smallest number should be converted into a 24 hour clock
    # find if either c or d is in the range but not both
    if abs(a - b) < 6:
        if a > b:
            b += 12
        else:
            a += 12
    arr = range(min(a,b), max(a,b) + 1)
    arr = [i - 12 if i > 12 else i for i in arr]
    if any([c in arr, d in arr]) and not all([c in arr, d in arr]):
        print("YES")
    else:
        print("NO")