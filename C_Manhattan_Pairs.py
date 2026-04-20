t = int(input())
for _ in range(t):
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y, i + 1))

    points.sort(key=lambda p: p[0] + p[1]) 

    for i in range(n // 2):
        print(points[i][2], points[n - 1 - i][2])
