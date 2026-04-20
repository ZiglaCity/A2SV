n = int(input())
s = input()
res = ""
count = 1
if len(s) <= 2:
    print(s)
else:
    i = 0
    while count <= len(s):
        res += s[count - 1]
        i += 1
        count += i
    print(res)