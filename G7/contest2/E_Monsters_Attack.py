t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))

    zipped = sorted(zip(a, x), key=lambda x: (abs(x[1]), x[0]))
    seconds = bullets  = 0
    prev_pos = 0

    for health, pos in zipped:
        bullets += ((abs(pos) - prev_pos) * k)
        if health > bullets:
            print("NO")
            break
        
        bullets -= health
        seconds += 1
        prev_pos = abs(pos)
    else:
        print("YES")
