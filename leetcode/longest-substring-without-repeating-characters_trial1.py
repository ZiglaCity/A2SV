class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = Counter()
        r = 0
        l = 0
        mx = 0
        while r < len(s):
            dic[s[r]] += 1
            if dic[s[r]] > 1:
                while dic[s[r]] > 1:
                    dic[s[l]] -= 1
                    l += 1
            mx = max(mx, r - l + 1)
            r += 1

        return mx