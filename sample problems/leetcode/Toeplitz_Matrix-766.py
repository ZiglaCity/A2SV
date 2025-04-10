def isToeplitzMatrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: bool
    """
    rows = len(matrix)
    colms = len(matrix[0])

    # first and last one are not really needed
    for d in range(rows + colms - 1):
        # r, c = (rows - d - 1, d) if d < rows else (0, d - rows + 1)
        r= rows - d - 1 if d < rows else 0
        c = 0 if d < rows else d - rows + 1        
        check = set()
        while r < rows and c < colms:
            check.add(matrix[r][c])
            r += 1
            c += 1
        print(check)
        if len(check) != 1:
            return False
    return True

# print(isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
# Output: True

print(isToeplitzMatrix([[1,2],[2,2]]))