def findDiagonalOrder( mat):
    """
    :type mat: List[List[int]]
    :rtype: List[int]
    """
    if not mat or not mat[0]:
        return []

    rows, cols = len(mat), len(mat[0])
    result = []
    for d in range(rows + cols - 1):
        if d % 2 == 0:
            # Even index diagonal (top-right to bottom-left)
            r, c = (d, 0) if d < rows else (rows - 1, d - rows + 1)
            while r >= 0 and c < cols:
                result.append(mat[r][c])
                r -= 1
                c += 1
        else:
            # Odd index diagonal (bottom-left to top-right)
            r, c = (0, d) if d < cols else (d - cols + 1, cols - 1)
            while r < rows and c >= 0:
                result.append(mat[r][c])
                r += 1
                c -= 1

    return result


# Example usage:
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]  
print(findDiagonalOrder(mat))  # Output: [1, 2, 4, 7, 5, 3, 6, 8, 9]
