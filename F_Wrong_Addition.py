# n = int(input())
# def check(a, s):
#     str_a = str(a)
#     str_s = str(s)
#     i = len(str_a) - 1
#     j = len(str_s) - 1
#     res = ""
#     while i >= 0 and j >= 0:
#         if int(str_s[j]) - int(str_a[i]) < 0 and j - 1 > 0:
#             print("Yes")
#             if (int(str_s[j] + str_s[j - 1]) - int(str_a[i])) > 9:
#                 return -1
#             res += str(int(str_s[j] + str_s[j - 1]) - int(str_a[i]))
#             j -= 1
#         else:
#             res += str(int(str_s[j]) - int(str_a[i]))
#             print("No")
#         i -= 1
#         j -= 1
#     return res


# for _ in range(n):
#     a, s = map(int, input().split())
#     print(check(a,s))


# intialize two pointrs
# check if a[i] > s[j]
#     add next element to the left (check for out of range index)
# perforem subtaction
# if we have excess numbers in s append them to the result
# removing leading zeros 
# if i is negative return answer else -1

# also when borrowing and after the subtraction there's a number greater than 10 there is a number greater than 10 check the eddge case