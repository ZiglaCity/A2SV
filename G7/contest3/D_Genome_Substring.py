n = int(input())
s = input()
target = "ACTG"

left = 0
right = 3
mn = float('inf')
while right < n:
    cur = 0
    j = 0
    for i in range(left, right + 1):
        diff = abs(ord(s[i]) - ord(target[j]))
        cur += min(diff, 26 - diff)
        j += 1
    mn = min(mn, cur)
    left += 1
    right += 1
print(mn)