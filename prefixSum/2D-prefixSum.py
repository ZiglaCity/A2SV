def prefixSum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    res = [[0] * cols for _ in range(rows)]
    for i in range(cols):
        res[0][i] += matrix[0][0] if i == 0 else matrix[0][i] + res[0][i - 1]

    for i in range(rows):  
        res[i][0] += 0 if i == 0 else res[i - 1][0] + matrix[i][0]

    for i in range(1, rows):
        for j in range(1, cols):
            res[i][j] = (res[i - 1][j] + res[i][j - 1] - res[i - 1][j - 1] + matrix[i][j])
    return res

if __name__ == '__main__':
    arr = [[3,2,1,4], [6,7,11,9], [0, 12, 8, 15], [3, -1, 20, -2]]
    ans = prefixSum(arr)
    for mat in ans:
        print(mat)