def check(x):
    for a in range(1, int(x ** (1/3)) + 2):
        a_cubed = a ** 3
        if a_cubed > x:
            break
        b_cubed = x - a_cubed
        b = round(b_cubed ** (1/3))
        if b > 0 and b ** 3 == b_cubed:
            return "YES"
    return "NO"


t = int(input())
results = []
for _ in range(t):
    x = int(input())
    print(check(x))