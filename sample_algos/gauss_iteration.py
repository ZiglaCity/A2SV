def get_matrix(row : int, col: int) -> list[list]:
    pass

def thomas_algorithm(A : list[list], d: list) -> list:
    # verify its a tridiagonal

    # let a(lower sub), b(main diagonal), c(upper sub) be the 3 diagonals
    # make b[1,1] = 1 by dividing row 1 by b[1,1]
    # from row 2 downwards;
    # make a[i, i - 1] 0's by Ri - a[i, i-1] * b[i -1, i - 1] .... this is possible because at each step the b[i-1,i -1] is made 1, hence helps eliminate a[i-1, i]
    # make b[i,i] 1 by Ri / b[i,i] - a[i, i-1] * c[i - 1, i] ( that is the current state of b[i, i] after eliminating the a[i, i - 1]) this makes the b[i, i] = 1, and takes care of the rest
    

    # perfor backward substitution to find the variables xi
    # focusing on, the start of the main diagonal of each row to the end
    # replace the found x, and use it in the subsequent calculations

    rows = len(A)
    cols = len(A[0])

    if not is_matrix_triadiagonal(A):
        print("Matrix is not triadiagonal hence can't be solved using the thomas algorithm")
        return

    X = [0] * cols
    b1 = A[0][0]
    for c in range(cols):
        A[0][c] /= float(b1)
    d[0] /= float(b1)

    for r in range(1, rows):
        a_i = A[r][r - 1]
        for c in range(r - 1, cols):
            c_i = A[r - 1][c]
            A[r][c] -= (a_i * c_i)
        
        b_i = float(A[r][r])
        for c in range(r, cols):
            A[r][c] /= b_i
        
        d[r] -= (a_i *  d[r- 1])
        d[r] /= b_i

    for r in range(rows - 1, -1, -1):
        rest = 0
        val = 0
        for c in range(r + 1, cols):
            rest += A[r][c] * X[c]
        val = d[r] - rest
        X[r] = val
    
    return X


def verify_final_X(X : list, A : list[list], d: list) -> list:
    res = [0] * len(d)
    for r in range(len(A)):
        val = 0
        for c in range(len(A[0])):
            # print(A[r][c], X[c])
            val += (A[r][c] * X[c])
        res[r] = val

    return res

def compare_the_Ds(initial_d : list, final_d : list) -> bool:
    for i in range(len(initial_d)):
        if int(initial_d[i]) != int(final_d[i]):
            print(f"WRONG {initial_d[i]} != {final_d[i]}")
            return False
    print(f"CORRECT {initial_d[i]} == {final_d[i]}")
    return True

            
def is_matrix_triadiagonal(matrix : list [list]) -> bool:
    return True

def gauss_jacobi_iteration(matrix: list[list]) -> list[list]:
    pass

def gauss_seidel_iteration(A: list[list], d: list) -> list:
    pass

if __name__ == "__main__":
    from test import test_thomas_algorithm
    test_thomas_algorithm()