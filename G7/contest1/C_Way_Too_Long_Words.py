t = int(input())
for _ in range(t):
    s = input()
    print(s if len(s) <= 10 else s[0] + str(len(s) - 2) + s[-1])