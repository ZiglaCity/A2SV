              
n, m = map(int, input().split())
mat = []
for _ in range(n):
    s = str(input())
    s = [char for char in s]
    mat.append(s)
row_counts = [{} for _ in range(n)]
col_counts = [{} for _ in range(m)]

for i in range(n):
    for j in range(m):
        row_counts[i][mat[i][j]] = row_counts[i].get(mat[i][j], 0) + 1
        col_counts[j][mat[i][j]] = col_counts[j].get(mat[i][j], 0) + 1

for i in range(n):
    for j in range(m):
        if row_counts[i][mat[i][j]] > 1 or col_counts[j][mat[i][j]] > 1:
            mat[i][j] = ""
for i in range(n):
    print("".join(mat[i]), end="")
            
                