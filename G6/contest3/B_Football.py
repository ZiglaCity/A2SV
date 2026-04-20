n = input()
def check(n):
    i = 1
    c = 1
    while i < len(n):
        if n[i] == n[i - 1]:
            c += 1
        else:
            c = 1
        if c >= 7:
            print("YES")
            return
        i += 1
    print("NO")

check(n)

