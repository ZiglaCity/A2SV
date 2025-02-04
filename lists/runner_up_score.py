if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    set_arr = set(arr)
    res = list(sorted(set_arr))
    if len(res) < 2:
        print(res[0])
    else:
        print(res[-2])