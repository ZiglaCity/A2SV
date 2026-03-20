class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        odd_count = 0

        for num in nums:
            if num % 2 == 1:
                odd_count += 1
            count += prefix_counts[odd_count - k]

            prefix_counts[odd_count] += 1

        return count

# class Solution:
#     def numberOfSubarrays(self, nums: List[int], k: int) -> int:
#         def atMostK(k: int) -> int:
#             count = 0
#             l = 0
#             odd_count = 0
            
#             for r in range(len(nums)):
#                 if nums[r] % 2 == 1:
#                     k -= 1
                
#                 while k < 0:  # Too many odd numbers, shrink window
#                     if nums[l] % 2 == 1:
#                         k += 1
#                     l += 1
                
#                 count += (r - l + 1)  # Add subarrays ending at r
            
#             return count
        
#         return atMostK(k) - atMostK(k - 1)
