n, m, k = map(int, input().split())
a = list(map(int, input().split()))
prefix = [0] * (n + 1)
operations = []
for _ in range(m):
    operation = list(map(int, input().split()))
    operations.append(operation)
# print(operations)

query = []
for _ in range(k):
    x, y = map(int, input().split())
    query.append([x - 1, y - 1])

q_prefix = [0] * (m + 1)

for x, y in query:
    q_prefix[x] += 1
    q_prefix[y + 1] -= 1

for i in range(1, len(q_prefix)):
    q_prefix[i] += q_prefix[i - 1]

for i in range(len(q_prefix) - 1):
    l = operations[i][0] -1
    r = operations[i][1] - 1
    d = operations[i][2]
    prefix[l] += (d * q_prefix[i]) 
    prefix[r + 1] -= (d * q_prefix[i])

a[0] += prefix[0]
for i in range(1, len(a)):
    prefix[i] += prefix[i - 1]
    a[i] += prefix[i]

print(*a)
