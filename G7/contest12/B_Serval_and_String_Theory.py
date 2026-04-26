t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    if k == 0:
        res = s < s[::-1]
    else:
        res = len(set(s)) != 1
    print("YES" if res else "NO")