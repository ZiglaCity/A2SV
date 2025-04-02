t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = sorted(arr)
    mn = float('inf')
    for i in range(n - 1):
        if arr[i] > min(arr[i+ 1:]):
            print('YES')
            break
        if i == n - 2:
            print("NO")
