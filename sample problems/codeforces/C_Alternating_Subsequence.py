t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.append(0)
    neg = arr[0] < 0
    largest = arr[0]
    sum_ = 0
    for i in range(1, n + 1):
        if neg :
            if arr[i] < 0:
                largest = max(largest, arr[i])
            else:
                neg = False
                sum_ += largest
                largest = arr[i]

        elif not neg:
            if arr[i] > 0:
                largest = max(largest, arr[i])
            else:
                neg = True
                sum_ += largest
                largest = arr[i]

    print(sum_)