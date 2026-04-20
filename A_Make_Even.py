t = int(input())
for _ in range(t):
    num = int(input())
    s = str(num)
    i = 0
    while i < len(s):
        if int(s[i]) % 2 == 0:
            break
        i += 1
    if int(s[-1]) % 2 == 0:
        print(0)
        continue
    elif int(s[0]) % 2 == 0:
        print(1)
        continue
    print(2 if i < len(s) else -1)