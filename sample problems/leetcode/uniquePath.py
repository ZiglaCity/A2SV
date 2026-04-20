def uniquePaths( m: int, n: int) -> int:

    memo = {}
    def check(r, c):
        if (r, c) in memo:
            print((r, c) , " Found in memo: ", (memo[(r, c)]))
            return memo[(r,c)]
        
        if r == m - 1 or c == n - 1:
            return 1
        
        val1 = check(r + 1, c) 
        val2 = check(r, c+ 1)
        memo[(r,c)] = val1 + val2
        # print(memo)
        return val1 + val2

    return check(0, 0)

m = 3
n = 7
print(uniquePaths(m, n)) 