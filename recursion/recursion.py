def check(n, cur):
    if cur > n:
        return False
    elif cur == n:
        return True
    val = check(n, cur * 4)
    return val

if __name__ == "__main__":
    n = 64
    print(check(n, 1))