class Solution:
    def sortEvenAndOddIndicesIndependently(self,nums):
        nums[1::2], nums[::2] = sorted(nums[1::2], reverse=True), sorted(nums[::2])
        return nums
    

if __name__ == "__main__":
    sol = Solution()
    nums = [4, 1, 2, 3]
    print(sol.sortEvenAndOddIndicesIndependently(nums))