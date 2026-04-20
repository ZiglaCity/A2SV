n = int(input())
# for each index we need 2 different loops
# each of the loops will also have 2 different loops
# inside the  2 sub loops on increases, when it get to the index, it starts decreasing
# the second sub loop starts decreasing, when it gets to 0 it stops
# we do the same for the second loop

total = (2 * n) + 1
k = 1
for i in range(n + 1):
    j = 0
    values = []
    while j <= i:
        values.append(j)
        j += 1
    j -= 2
    while j >= 0:
        values.append(j)
        j -= 1
    space = (total - len(values)) // 2
    for i in range(space):
        print(" " * 2, end="")
    print(*values)

for i in range(n - 1, -1, -1):
    j = 0
    values = []
    while j <= i:
        values.append(j)
        j += 1
    j -= 2
    while j >= 0:
        values.append(j)
        j -= 1
    space = (total - len(values)) // 2
    for i in range(space):
        print(" " * 2, end="")
    print(*values)
