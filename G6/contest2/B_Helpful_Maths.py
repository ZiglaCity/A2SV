n = input().split('+')
n.sort()
res = ""
for num in n:
    res += num + "+"
print(res[:-1])