class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        for s in strs[1:]:
            i = 0
            while i < len(prefix) and i < len(s):
                if s[i] != prefix[i]:
                    prefix = prefix[0:i:]
                    break
                i +=1
            else:
                prefix = prefix[:i]
        return prefix