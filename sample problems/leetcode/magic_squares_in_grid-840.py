class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total = 0

        rows = len(grid)
        colms = len(grid[0])

        def culm_sums(row, col, res):
            for c in (col - 1, col, col + 1):
                if sum(grid[row + i][c] for i in (-1, 2) ) != res:
                    return False
                pass
            return True
        
        def row_sums(row, col, res):
            if res == sum(grid[r - 1][c - 1: c + 2 ]) and \
                res == sum(grid[r + 1][c - 1: c + 2 ]):
                return True
            return False

        def diagonal_sums(row, col, res):
            if res == sum(grid[row + i][col + i] for i in range(-1, 2)) and \
               res == sum(grid[row + i][col - i] for i in range(-1, 2)):
                return True
            return False

        for r in range(1, rows - 1):
            for c in range(1, colms - 1):
                res = sum(grid[r][c - 1: c + 2])
                if culm_sums(r, c, res) and row_sums(r, c, res) \
                    and diagonal_sums(r, c, res):
                    total += 1

        return total