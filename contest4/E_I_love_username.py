n = int(input())
arr = list(map(int, input().split()))
mn = arr[0]
mx = arr[0]
count = 0
for i in range(1, len(arr)):
    if arr[i] < mn:
        mn = arr[i]
        count += 1
    elif arr[i] > mx:
        mx = arr[i]
        count += 1
print(count)