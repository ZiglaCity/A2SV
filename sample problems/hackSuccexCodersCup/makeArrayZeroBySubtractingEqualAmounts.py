class Solution:
    def makeArrayZeroBySubtractingEqualAmounts(self, nums):
        return len(set([val for val in nums if val != 0]))    


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 5, 0, 3, 5]
    print(sol.makeArrayZeroBySubtractingEqualAmounts(nums))