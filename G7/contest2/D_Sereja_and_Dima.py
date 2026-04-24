n = int(input())
a = list(map(int, input().split()))

s, d = 0, 0
left, right = 0, n - 1
serge_turn = True
while left <= right:
    if serge_turn:
        s += max(a[left], a[right])
        if a[left] > a[right]:
            left += 1
        else:
            right -= 1
    else:
        d += max(a[left], a[right])
        if a[left] > a[right]:
            left += 1
        else:
            right -= 1
    serge_turn = not serge_turn

print(s, d)    