class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        target = Counter(p)
        newDic = Counter(s[:len(p)])
        res = []
        if target == newDic:
            res.append(0)
        
        for i in range(len(s) - len(p)):
            newDic[s[i]] -= 1
            newDic[s[i + len(p)]] += 1
            if newDic == target:
                res.append(i + 1)
        return res
