n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

count = 0
res = []
for num in arr2:
    while count < len(arr1) and arr1[count] < num:
        count += 1
    res.append(count)
print(*res)
