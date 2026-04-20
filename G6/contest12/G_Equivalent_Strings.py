a = input()
b = input()

if a[::-1] == b or a == b:
    print("YES")
elif sorted(a) != sorted(b):
    print("NO")
else:

    def check(x, y):
        if x == y:
            return True
        if len(x) % 2 or len(y) % 2:
            return False
        mid = len(x) // 2
        x1, x2 = x[:mid], x[mid:]
        y1, y2 = y[:mid], y[mid:]
        return (check(x1, y1) and check(x2, y2)) or (check(x1, y2) and check(x2, y1))

    print("YES" if check(a, b) else "NO")
