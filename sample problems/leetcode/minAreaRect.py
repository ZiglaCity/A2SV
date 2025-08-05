class Solution:
    def minAreaRect(self, points):
        from collections import defaultdict
        dic = defaultdict(list)
        for x, y in points:
            dic[x].append(y)
        res = float('inf')
        for x1, y1s in dic.items():
            for x2, y2s in dic.items():
                area = 0
                if x != x2:
                    valid = set(y1s) & set(y2s)
                    if len(valid) >= 2:
                        area = abs(list(valid)[0] - list(valid)[1]) * abs(x1 - x2)
                if area != 0:
                    res = min(res, area)
        return res
    


if __name__ == "__main__":
    sol = Solution()
    input = [[1,1],[1,3],[3,1],[3,3],[2,2]]
    print(sol.minAreaRect(input))

    input = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
    print(sol.minAreaRect(input))
