n = int(input()) + 1
s = str(n)
while len(set(s)) < 4:
    n += 1
    s = str(n)
print(n)

