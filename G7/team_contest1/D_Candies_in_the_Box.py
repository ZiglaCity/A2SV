n, k = map(int, input().split())

res = 0
for i in range(1, n + 1):
    res += i 
    if res - k == n - i:
        print(n - i)
        break