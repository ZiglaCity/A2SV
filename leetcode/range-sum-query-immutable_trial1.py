class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = nums[:1]
        for i in range(1, len(nums)):
            self.prefix.append(self.prefix[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right] if left == 0 else self.prefix[right] - self.prefix[left - 1]
    


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)