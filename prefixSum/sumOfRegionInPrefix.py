class NumMatrix:

    def __init__(self, matrix):
        self.prefixSum = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix[0])):
            self.prefixSum[0][i] = matrix[0][0] if i == 0 else self.prefixSum[0][i - 1] + matrix[0][i]
        
        for i in range(1, len(matrix)):
            self.prefixSum[i][0] = self.prefixSum[i - 1][0] + matrix[i][0]
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                self.prefixSum[i][j] = self.prefixSum[i - 1][j] + self.prefixSum[i][j - 1] - self.prefixSum[i - 1][j - 1] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res =  self.prefixSum[row2][col2] if row1 == 0 else self.prefixSum[row2][col2] - self.prefixSum[row1 - 1][col2]
        res -= 0 if col1 == 0 else self.prefixSum[row2][col1 - 1] 
        res += 0 if (row1  == 0 or col1 == 0) else self.prefixSum[row1 - 1][col1 - 1] 
        print(self.prefixSum)
        return res

if __name__ == '__main__':
    mat = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    obj = NumMatrix(mat)

    print(obj.sumRegion(2, 1, 4, 3))