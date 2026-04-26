n = int(input())
a = list(map(int, input().split()))
q = int(input())

dic = {}
qs = []
for i in range(q):
    x = list(map(int, input().split()))

    if len(x) == 3:
        p, v = x[1], x[2]
        a[p - 1] = v
        dic[p - 1] = i
        qs.append(0)
    else:
        qs.append(x[1])
    
mx = max(qs)
for i in range(len(qs) - 2, -1, -1):
    qs[i] = max(qs[i], qs[i + 1])

for i in range(n):
    if i in dic:
        last = dic[i]
        a[i] = max(a[i], qs[last])
    else:
        a[i] = max(a[i], mx)

print(*a)
    

    