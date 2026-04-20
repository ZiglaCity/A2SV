# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))

#     # within k operations, choose any index i, and any integer p, and replace ai with p
#     #  if k is 0 it means we do a total of len(set(a)) deletion
#     # keep a dic of the total freq of each number
#     # for every i in k, 
#     # change every number from the smallest freq into the large freq
#     # when k finishes we check how many elements are still left in the dic

#     dic = {}
#     for num in a:
#         dic[num] = dic.get(num, 0) + 1
        
#     smallest_array = []
#     for num in dic:
#         smallest_array.append([num, dic[num]])
    
#     smallest_array.sort(key=lambda x: x[1])

#     i = 0
#     while k > 0:
#         if smallest_array[i][1] <= k:
#             k -= smallest_array[i][1]
#             smallest_array[i][1] = 0
#             i += 1
#         else:
#             break
    
#     total = 0
#     for num, freq in smallest_array:
#         if freq > 0:
#             total += 1
    
#     print(total if total > 0 else 1)

# the above appraoch leads to TLE for large inputs, an optimal solution can be seen below


def gorillaExam(n, k, a):
    a.sort()
    freq = []
    for i in range(n):
        if i > 0 and a[i] == a[i - 1]:
            freq[len(freq) - 1] += 1
        else:
            freq.append(1)

    freq.sort()
    i = 0
    while k > 0 and i < len(freq) - 1:
        if freq[i] <= k:
            k -= freq[i]
            i += 1
        else:
            break

    return len(freq) - i


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(gorillaExam(n, k, a))