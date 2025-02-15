n = int(input())
arrs = []
for _ in range(n):
    len_a = int(input())
    arr = list(map(int, input().split()))
    arrs.append(arr)

for ar in arrs:
    for i in range(1, len(ar)):
        while int((ar[i] / ar[i - 1])) == (ar[i] / ar[i -1]):
            ar[i - 1] += 1
print(arrs)