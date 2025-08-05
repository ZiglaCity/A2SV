class Solution:
    def findUniqueDestination(self, paths):
        s = set()
        for a, b in paths:
            s.add(b)

        for a, b in paths:
            if a in s:
                s.remove(a)

        return list(s)[0]

    
if __name__ == "__main__":
    paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
    sol = Solution() 
    print(sol.findUniqueDestination(paths))