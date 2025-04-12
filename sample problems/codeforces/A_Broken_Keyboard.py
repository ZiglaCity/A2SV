t = int(input())

for _ in range(t):
    s = input()
    dict = {}
    for char in s:
        dict[char] = dict.get(char, 0) + 1
    res = []
    for v in dict:
        if dict[v] % 2 == 1:
            res.append(v)
    res.sort()
    print("".join(res))


