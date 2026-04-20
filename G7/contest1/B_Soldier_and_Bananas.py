k, n , w = map(int, input().split())

total = 0
for i in range(1, w + 1):
    total += (i * k)

print(max(0, total - n))