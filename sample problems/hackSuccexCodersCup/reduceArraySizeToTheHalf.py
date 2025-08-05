from collections import defaultdict


class Solution:
    def reduceArraySizeToTheHalf(self, arr):
        n = len(arr)
        dic = defaultdict(int)
        for num in arr:
            dic[num] += 1
        
        arr = sorted(list(set(arr)),key=lambda x: -dic[x])
        i = 0
        half = n // 2
        while n > half:
            n -= dic[arr[i]]
            i += 1
        return i


if __name__ == "__main__": 
    sol = Solution()
    arr = [3,3,3,3,5,5,5,2,2,7]
    print(sol.reduceArraySizeToTheHalf(arr))