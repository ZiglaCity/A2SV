class Solution:
    def isRowsAndColsUnique(self, matrix):
        n = len(matrix)
        for i in range(len(matrix)):
            rows = set()
            cols = set()
            for j in range(len(matrix)):
                rows.add(matrix[i][j])
                cols.add(matrix[j][i])
            if len(rows) != n or len(cols) != n:
                return False
        return True



if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3],[3, 1, 2],[2, 3, 4]]
    print(sol.isRowsAndColsUnique(matrix))
