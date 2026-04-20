n = int(input())
arr = []
for _ in range(n):
    a, s = map(int, input().split())
    arr.append((a,s))
print(arr)

# intialize two pointrs
# check if a[i] > s[j]
#     add next element to the left (check for out of range index)
# perforem subtaction
# if we have excess numbers in s append them to the result
# removing leading zeros 
# if i is negative return answer else -1

# also when borrowing and after the subtraction there's a number greater than 10 there is a number greater than 10 check the eddge case