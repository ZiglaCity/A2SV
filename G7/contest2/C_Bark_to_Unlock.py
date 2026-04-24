s = input()
n = int(input())

last = set()
first = set()
seen = False

for _ in range(n):
    w = input()
    if set(w) == set(s):
        seen = True
    last.add(w[1])
    first.add(w[0])

if seen:
    print("YES")
else:
    print("YES" if s[0] in last and s[1]  in first else "NO")