q = int(input())
for _ in range(q):
    arr = [tuple(map(int, input().split()))]

    for a, b, c in arr:
        min_distance = float('inf')
        for da in range(-1, 2):
            for db in range(-1, 2):
                for dc in range(-1, 2):
                    a_new = a + da
                    b_new = b + db
                    c_new = c + dc
                    distance = abs(a_new - b_new) + abs(a_new - c_new) + abs(b_new - c_new)
                    min_distance = min(min_distance, distance)
        print(min_distance)