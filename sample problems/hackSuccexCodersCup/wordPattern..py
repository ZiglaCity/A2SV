class Solution:
    def wordPattern(self,pattern, s):
        dic = {}
        words = s.split()
        if len(words) != len(pattern):
            return False
        for i in range(len(words)):
            if words[i] in dic:
                if dic[words[i]] != pattern[i]:
                    return False
            else:
                dic[words[i]] = pattern[i]
        
        return True


    def wordPattern2(self, pattern, s):
        dic = {}
        words = s.split()
        if len(words) != len(pattern):
            return False
        for i in range(len(words)):
            dic[words[i]] = pattern[i]
        
        p = []
        for word in words:
            p.append(dic[word])
        return p == list(pattern)



if __name__ == "__main__":
    sol = Solution()
    pattern = "abba"
    s = "dog cat cat dog"
    print(sol.wordPattern(pattern, s))