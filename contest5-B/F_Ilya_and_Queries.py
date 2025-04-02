s = input()
arr = []
arr.append(0)
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        arr.append(arr[i- 1] + 1)
    else:
        arr.append(arr[i - 1])
m = int(input())
for _ in range(m):
    l, r = map(int, input().split())
    print(arr[r - 1] - arr[l - 1])
