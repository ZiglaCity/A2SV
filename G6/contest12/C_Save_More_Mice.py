t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort(reverse=True)
    saved = cat = 0
    for mouse in x:
        if mouse > cat:
            saved += 1
            cat += n - mouse
            if cat >= n:
                break
        else:
            break
    print(saved)
