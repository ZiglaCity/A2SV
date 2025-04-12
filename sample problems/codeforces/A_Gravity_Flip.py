n = int(input())
a = list(map(int, input().split()))

i = n - 1
while i > 0:
    highest = max(a[:i + 1]) 
    highest_index = a.index(highest)
    if highest_index < i:
        cur = a[i]
        a[i] += (highest - a[i])
        a[highest_index] -= (highest - cur)
    i -= 1
print(*a)
    