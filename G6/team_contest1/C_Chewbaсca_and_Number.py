t = str(input())
res = ""
for i in range(len(t)):
    if i == 0 and t[i] == "9":
        res += t[i]
        continue
    if int(t[i]) >= 5:
        res += str(9 - int(t[i]))
    else:
        res += t[i]
print(int(res))