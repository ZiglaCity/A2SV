from gauss_iteration import thomas_algorithm, verify_final_X, compare_the_Ds

def test_thomas_algorithm():
    A = [[3, 2, 0, 0], [2, 3, 2, 0], [0, 2, 3, 2], [0, 0, 2, 3]]
    matrix = [[r for r in row] for row in A]
    d = [12, 17, 14, 7]
    d_sample = [num for num in d]
    res = thomas_algorithm(A, d)
    print("Final Result: X = ", res)
    final_d = verify_final_X(res, matrix, d)
    compare_the_Ds(initial_d=d_sample, final_d=final_d)
    print("Verified d = ", final_d)
