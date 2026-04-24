t = int(input())

for _ in range(t):
    n = int(input())
    if n <= 3:
        print(n)
    else:
        print(n % 2)