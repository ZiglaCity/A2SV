# k = int(input())
# dic = {}
# for i in range(k):
#     # get each of the sequences
#     length = int(input())
#     arr = list(map(int, input().split()))
#     dic[i + 1] = arr

# for i in dic:
#     for j in dic:
#         if i != j:
#             sum_i = sum(dic[i])
#             sum_j = sum(dic[j])
#             for element in dic[i]:
#                 new_sum = sum_i - element
#                 for e in dic[j]:
#                     if new_sum == sum_j - e:
#                         print(new_sum)
#                         print(sum_j - e)
#                         print("YES")
#                         print(i, dic[i].index(element) + 1)
#                         print(j, dic[j].index(e) + 1)
                
# print("NO")

# pick two sequence such that;
# we can remove one from i and one from j and their sums would be equal