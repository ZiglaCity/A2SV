class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        s = set(nums)
        for num in sorted(list(s)):
            nums[i] = num
            i += 1
        return len(s)