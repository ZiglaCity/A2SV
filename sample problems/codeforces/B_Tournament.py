t = int(input())
for _ in range(t):
    n, j, k = map(int, input().split())
    a = list(map(int, input().split()))
    if k != 1:
        print("YES")
    else:
        print("YES" if a[j - 1] == max(a) else "NO")