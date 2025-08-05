class Solution:
    def maxScoreFromRemovingStones(self, a,b,c):
        res = 0
        vals = sorted([ val for val in [a, b, c] if val > 0])
        while len(vals) > 1:
            vals[-1] -= 1
            vals[-2] -= 1
            res += 1
            vals = sorted([val for val in vals if val > 0])

        return res


if __name__ == "__main__":
    sol = Solution()
    a = 3
    b = 4
    c = 5
    print(sol.maxScoreFromRemovingStones(a, b, c ))