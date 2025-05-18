n = int(input())
arr = list(map(int, input().split()))
if n == 1:
    print(1, 0)
elif n == 2:
    print(1, 1)
else:
    l = 0
    r = n - 1
    b = arr[r]
    a = arr[l]
    l += 1
    alice = 1
    r -= 1
    bob = 1
    while l < r:
        if a > b:
            b += arr[r]
            r -= 1
            bob += 1
        else:
            a += arr[l]
            l += 1
            alice += 1

    if a > b:
        bob += 1
    else:
        alice += 1

    print(alice, bob)