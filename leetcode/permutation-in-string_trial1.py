class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dic = defaultdict(int)
        for char in s1:
            s1_dic[char] += 1
        s2_dic = defaultdict(int)
        l = 0

        for r in range(len(s2)):
            s2_dic[s2[r]] += 1

            while s2_dic[s2[r]] > s1_dic[s2[r]]:
                s2_dic[s2[l]] -= 1
                l += 1
            
            if s2_dic == s1_dic:
                return True

        return False