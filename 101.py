import numpy as np

def generating_function(n):
    return 1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10
    # return n**3


def get_linear_equation(variables, n):
    coeffs = []
    for i in range(0, variables):
        coeffs.append(n**i)
    return coeffs


def solve_equations(visible_terms):
    equations_coeffs = []
    values = []
    for n in range(1, visible_terms + 1):
        equations_coeffs.append(get_linear_equation(visible_terms, n))
        values.append(generating_function(n))

    A = np.array(equations_coeffs)
    B = np.array(values)
    X = np.linalg.solve(A, B)

    # This will return solved values from constant to highest coefficient from left to right
    return X.tolist()


max_bops = 10
answer = 0
for bop in range(1, max_bops + 1):
    bop_coeffs = solve_equations(bop)
    # print(bop_coeffs)
    evaluating_for = bop + 1
    for i in range(0, bop):
        answer += bop_coeffs[i]*(evaluating_for**i)

print(int(answer))