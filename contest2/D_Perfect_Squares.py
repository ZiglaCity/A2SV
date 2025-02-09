n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
for i in range(len(arr)):
    if arr[i] > 0:
        root = pow(arr[i], 0.5)    
        if round(root) != root:
            print(arr[i])
            break
    if arr[i] < 0:
        print(arr[i])
        break