n = int(input())
arrs = []
for _ in range(n):
    l, r = map(int, input().split())
    arrs.append((l,r))

for arr in arrs:
    mx = 0
    l = max(arr)
    r = min(arr)
    for i in range(r, l + 1):
        luckiness = int(max(str(i))) - int(min(str(i)))
        if max(mx, luckiness) > mx:
            mx = max(mx, luckiness) 
            num = i
    print(num)