n = int(input())
arrs = []
for _ in range(n):
    len_a = int(input())
    arr = list(map(int, input().split()))

    for i in range(len(arr)):
        if arr[i] == 1:
            arr[i] += 1

    for i in range(1, len(arr)):  
        if arr[i] % arr[i -1] == 0:
            arr[i] += 1
    
    for x in arr:
        print(x, end=" ")
    print()
