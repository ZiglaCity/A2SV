password = input().strip()
n = int(input())
arr = []
for _ in range(n):
    s = input().strip()
    arr.append(s)

def check(arr):
    if password in arr:
        print("YES")
        return
    elif arr[0][0] + arr[0][1] == password or arr[0][1] + arr[0][0] == password:
        print("YES")
        return
    else:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][1] + arr[j][0] == password or arr[j][1] + arr[i][0] == password:
                    print("YES")
                    return 
    print("NO")
check(arr)
            
            
        