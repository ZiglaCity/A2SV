class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first = second = 0
        res = []
        for i, j in firstList:
            for x, y in secondList:
                if j >= x and i <= y:
                    res.append([max(i, x),  min(j, y)])
                if j < x:
                    break  
        return res
