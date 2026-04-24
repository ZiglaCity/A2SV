t = int(input())
for _ in range(t):
    n, m, p, q = map(int, input().split())
    if not n % p:
        print("YES" if (n // p) * q == m else "NO")
    else:
        print("YES")