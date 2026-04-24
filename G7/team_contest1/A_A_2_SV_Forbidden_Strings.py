n = int(input())

res = set()
def recurse(cur):
    if len(cur) == n:
        res.add(tuple(cur))
        return

    for c in "ASV":
        if len(cur) >= 1 and cur[-1] == c:
            continue
        if len(cur) >= 2 and cur[-2:] == ["S", "V"] and c == "A":
            continue
        recurse(cur[::] + [c])

recurse([])
print(len(res))
# print(res)