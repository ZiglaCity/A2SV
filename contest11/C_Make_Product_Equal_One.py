n = int(input())
arr = list(map(int, input().split()))

cost = 0
negs = 0
zeros = 0

for num in arr:
    if num > 0:
        cost += num - 1
    elif num < 0:
        cost -= num + 1
        negs += 1
    else:
        zeros += 1
        cost += 1

if negs % 2 == 1 and zeros == 0:
    cost += 2

print(cost)
