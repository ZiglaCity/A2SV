def inclusivePrefixSum( nums):
    res = nums[:1]
    for i in range(1, len(nums)):
        res.append(res[-1] + nums[i])
    return res

def exclusivePrefixSum(nums):
    res = [0]
    for i in range(len(nums) - 1):
        res.append(res[-1] + nums[i])
    return res


if __name__ == '__main__':
    nums = [4,7,3,4,7,8,9,4,3,2,5,6,33,1,3,5,8,4,7,3]
    print(inclusivePrefixSum(nums))
    print(exclusivePrefixSum(nums))