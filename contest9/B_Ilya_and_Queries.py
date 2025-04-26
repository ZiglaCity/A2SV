s = str(input())
m = int(input())
prefix = [0] * len(s)
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        prefix[i] = 1
    prefix[i] += prefix[i - 1]

for _ in range(m):
    l, r = map(int, input().split())
    print(prefix[r - 1] - prefix[l -  1])