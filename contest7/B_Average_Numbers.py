n = int(input())
a = list(map(int, input().split()))
count = 0
arr = []
total = sum(a)
# get each number in the array
# multiply each number by the total sum 
# subtract the rest of the numbers form the value
# if the current number equals the result
# keep track of its index
for i in range(n):
    product = a[i] * n
    rest = total - a[i]
    new_value = product - rest
    if new_value == a[i]:
        count += 1
        arr.append(i + 1)
print(len(arr))
if len(arr):
    print(*arr)

    