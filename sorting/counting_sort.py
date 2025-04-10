# we count the number of occurence of each elemment and store it in an array using that number as an index
def counting_sort(nums):
    mx = max(nums)
    count = [0] * (mx + 1)

    for num in nums:
        count[num] += 1
    
    res = []
    for i in range(len(count)):
        j = count[i]
        while j > 0:
            res.append(i)
            j -= 1

    return res
 

# counting sort to sort numbers with both negative and postive in it
def counting_sort2(nums):
    mx = max(nums)
    mn = min(nums)

    size = mx - mn + 1
    count = [0] * size
    
    for num in nums:
        count[num - mn] += 1
    
    res = []
    for i in range(len(count)):
        j = count[i]
        while j > 0:
            value = i + mn
            res.append(value)
            j -= 1

    return res


if __name__ == '__main__':
    nums = [-2, -3, -3, -5,  5, 3, 3, 3, 2, 3, 4, 2, 5, 1]
    nums2 = [3, 2, 1, 4, 5, 3, 2, 1, 0, 2, 5, 6]
    # output: [-5, -3, -3, -2, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5]
    print(counting_sort2(nums))
    # output: [0, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 6]
    print(counting_sort(nums2))
    
