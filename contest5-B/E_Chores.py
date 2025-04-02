n, k, x = map(int, input().split())
arr = list(map(int, input().split()))
res = x * k
for i in range(n - k):
    res += arr[i]
print(res)