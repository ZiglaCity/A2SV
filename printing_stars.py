def print_star1(n):
    for i in range(1, n + 1):
        print('*' * i)


def print_star2(n):
    start = n // 2
    for i in range(1, n + 1):
        if i % 2 == 1:
            s = "*" * i
            print(" " * start + s)
            start -= 1



def print_star3(n):
    half = n // 2 + 1
    halfed = False
    stars = 0
    for i in range(1, n + 1):
        if half == 0:
            halfed = True
        if halfed:
            stars -= 1
            print(" " * (n// 2 + 1 - stars) + "*" * stars)
        else:
            half -= 1
            stars += 1
            print(" " * (n// 2 + 1 - stars) + "*" * stars)


if __name__ == "__main__":
    n = int(input())
    print_star1(n)
    print("")
    print_star2(n)
    print('')
    print_star3(n)