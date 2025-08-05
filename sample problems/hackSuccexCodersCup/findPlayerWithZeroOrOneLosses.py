from collections import defaultdict
class Solution:
    def findPlayerWithZeroOrOneLosses(self, matches):
        dic = defaultdict(int)
        for winner, loser in matches:
            dic[loser] += 1
            if winner not in dic:
                dic[winner] = 0
        
        res = [[],[]]
        for p in dic:
            if dic[p] == 0:
                res[0].append(p)
            elif dic[p] == 1:
                res[1].append(p)

        return [sorted(res[0]), sorted(res[1])]

if __name__ == "__main__":
    sol = Solution()
    matches = [[1,3], [2,3],[3, 6], [5, 6], [5, 7],[4, 5], [4, 8],[4, 9], [10, 4], [10, 9]]
    print(sol.findPlayerWithZeroOrOneLosses(matches))