class Solution:
    def largestSquare(self, rectangles):
        squares = [min(a,b) for a, b in rectangles]
        # same as below
        squares_ = list(map(min, rectangles))
        largest = max(squares)
        count = 0
        for sq in squares:
            if sq == largest:
                count += 1
        return count
    


if __name__ == "__main__":
    sol = Solution()
    rectangles = [[5, 8],[3, 9], [5, 12], [16, 5]]
    print(sol.largestSquare(rectangles))
