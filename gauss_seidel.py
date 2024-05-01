# Not mine

def gauss_seidel(a_matrix, b, x, n, tol):
    max_iterations = 1000000
    x_prev = [0.0 for _ in range(n)]
    for i in range(max_iterations):
        for j in range(n):
            x_prev[j] = x[j]
        for j in range(n):
            summ = 0.0
            for k in range(n):
                if k != j:
                    summ = summ + a_matrix[j][k] * x[k]
            x[j] = (b[j] - summ) / a_matrix[j][j]
        diff1norm = 0.0
        old_norm = 0.0
        for j in range(n):
            diff1norm = diff1norm + abs(x[j] - x_prev[j])
            old_norm = old_norm + abs(x_prev[j])
        if old_norm == 0.0:
            old_norm = 1.0
        norm = diff1norm / old_norm
        if (norm < tol) and i != 0:
            print("Sequence converges to [", end="")
            for j in range(n - 1):
                print(x[j], ",", end="")
            print(x[n - 1], "]. Took", i + 1, "iterations.")
            return
    print("Doesn't converge.")


if __name__ == '__main__':
    matrix2 = [[3.0, 1.0], [2.0, 6.0]]
    vector2 = [5.0, 9.0]
    guess = [0.0, 0.0]
    
    matrix3 = [[9.0, -3.0], [-2.0, 8.0]]
    vector3 = [6.0, -4.0]
    
    matrix4 = [[1.0, -3.0], [-2.0, 8.0]]

    gauss_seidel(matrix2, vector2, guess, 2, 0.00000000000001)
    gauss_seidel(matrix3, vector3, guess, 2, 0.00000000000001)
    gauss_seidel(matrix4, vector3, guess, 2, 0.00000000000001)
