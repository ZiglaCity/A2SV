r1 = list(map(int, input().split()))
r2 = list(map(int, input().split()))    
r3 = list(map(int, input().split()))

arr = [r1, r2, r3]
init = [[1,1,1], [1,1,1], [1,1,1]]
# if theres an even number then we dont do any thing since toggling it will just return the same value
# if theres an odd number then we toggle it and its neighbors making sure we dont go out or range
for i in range(3):
    for j in range(3):
        if arr[i][j] % 2 != 0:
            init[i][j] = 0 if init[i][j] == 1 else 1
            if i > 0:
                init[i - 1][j] = 0 if init[i - 1][j] == 1 else 1
            if i < 2:
                init[i + 1][j] = 0 if init[i + 1][j] == 1 else 1
            if j > 0:
                init[i][j - 1] = 0  if init[i][j - 1] == 1 else 1
            if j < 2:
                init[i][j + 1] = 0 if init[i][j + 1] == 1 else 1
for element in init:
    print("".join(map(str, element)))