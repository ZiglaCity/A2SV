i = j = 0
for x in range(5):
    arr = list(map(int, input().split()))
    if 1 in arr:
        i = x
        j = arr.index(1)
        break

print(abs(3 - (i + 1)) + abs(3 - (j + 1)))