class Solution:
    def checkStrings(self, s1, s2):
        count = 0
        set1 = set()
        set2 = set()
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
            set1.add(s1[i])
            set2.add(s2[i])
        return set1 == set2 and count <= 2



if __name__ == "__main__":
    sol = Solution()
    s1 = "bank"
    s2 = "kanb"
    print(sol.checkStrings(s1, s2))