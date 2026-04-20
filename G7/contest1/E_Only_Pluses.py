t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    
    for i in range(5):
        if a == min(a, b, c):
            a += 1
        elif b == min(a, b, c):
            b += 1
        else:
            c += 1
        
    print(a * b * c)