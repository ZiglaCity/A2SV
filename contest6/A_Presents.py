n = int(input())
p = list(map(int, input().split()))
#  the number of a friend who gave a gift to friend number i
arr = []
for i in range( n):
    arr.append((i + 1, p[i]))
sorted_arr = sorted(arr, key=lambda x: x[1])
for element in sorted_arr:
    print(element[0], end=" ")