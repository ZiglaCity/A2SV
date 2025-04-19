t = int(input())
for _ in range(t):
    res = []
    start = False
    printed = False
    space = input()
    for i in range(8):
        arr = list(map(str, input().split()))
        arr = [char for char in arr[0]]

        if arr.count('#') == 2:
            start = True
        
        if start and arr.count('#') == 1 and not printed:
            print(i + 1, arr.index('#') + 1)
            printed = True
            
        
    if not start:
        print(1, arr.index('#') + 1)
