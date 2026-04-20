t = int(input())
for i in range(t):
    n = int(input())
    s = input()[::-1]
    c = 0
    for j in range(n):
        if s[j] != ')':
            break
        c += 1
    print("Yes" if c > n - c else "No")