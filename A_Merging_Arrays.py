n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

i = 0
j = 0
arr = []
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        arr.append(arr1[i])
        i += 1
    else:
        arr.append(arr2[j])
        j += 1

print(*(arr + arr1[i:] + arr2[j:]))