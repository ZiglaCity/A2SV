def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    top, left = 0, 0
    right, down = len(matrix[0]), len(matrix)
    res = []
    while left < right and top < down:
        # iterate the top where j changes to the right
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1
        # iterate the right where i changes to the down
        for i in range(top, down):
            res.append(matrix[i][right - 1])
        right -= 1
        # iterate the down where j changes to the left
        for i in range(right - left - 1, left - 1, -1):
            res.append(matrix[down - 1][i])
        down -= 1
        # iterate the left wehre i chagnes to the top
        for i in range(down - top, top - 1, -1):
            res.append(matrix[i][left])
        left += 1
    return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))