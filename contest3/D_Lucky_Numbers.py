n = int(input())
arrs = []
def check(l, r):
    max_diff = -1
    lucky = l
    for i in range(min(l, r), max(l, r) + 1):
        mx = max(str(i))
        mn = min(str(i))
        if max_diff < max(max_diff, abs(int(mx) - int(mn))):
            max_diff = max(max_diff, abs(int(mx) - int(mn)))
            lucky = i
        if max_diff == 9:
            return i
    return lucky
            
for _ in range(n):
    l, r = map(int, input().split())
    print(check(l,r))

    

