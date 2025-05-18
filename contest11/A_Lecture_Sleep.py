n, k = map(int, input().split())
arr = list(map(int, input().split()))
t = list(map(int, input().split()))

ones = sum(arr[i] for i in range(n) if t[i] == 1)
mx = 0
zeros = sum(arr[i] for i in range(k) if t[i] == 0)

mx = zeros

for i in range(k, n):
    if t[i] == 0:
        zeros += arr[i]
    if t[i - k] == 0:
        zeros -= arr[i - k]
    mx = max(mx, zeros)

print(ones + mx)