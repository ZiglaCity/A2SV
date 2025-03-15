k, n, w = map(int, input().split())
cost = 0
for i in range(1, w + 1):
    cost += (i * k)
print(abs(cost - n) if n < cost else 0)