class Solution:
    def maxBagsWithFullCapacityOfRocks(self,capacity, rocks,additionalRocks):
        capacity = sorted([capacity[i] - rocks[i] for i in range(len(capacity))])
        res = 0
        for i in range(len(capacity)):
            if capacity[i] <= additionalRocks and capacity[i] <= additionalRocks:
                res += 1
                additionalRocks -= capacity[i]
            if capacity[i] > additionalRocks:
                return res
        return res
    


if __name__ == "__main__":
    sol = Solution()
    capacity = [2, 3, 4, 5]
    rocks = [1, 2, 4, 4]
    additionalRocks= 2
    print(sol.maxBagsWithFullCapacityOfRocks(capacity, rocks, additionalRocks))