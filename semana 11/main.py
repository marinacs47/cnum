import numpy as np
from scipy.differentiate import derivative

from algoritmos import dp, dr, dc


def main():
    # Atividade 1
    print("-- Atividade 1 --")

    h1 = 1e-2
    h2 = 1e-3
    eps = np.finfo(float).eps

    print("f(x) = sin(x)")

    f = lambda x: np.sin(x)

    print("Diferença progressiva:")
    print("h = 0.01 | f'(x)=", dp(f, 2, h1))
    print("h = 0.001 | f'(x)=", dp(f, 2, h2))
    print("h = eps | f'(x)=", dp(f, 2, np.sqrt(eps)))

    print("Diferença regressiva:")
    print("h = 0.01 | f'(x)=", dr(f, 2, h1))
    print("h = 0.001 | f'(x)=", dr(f, 2, h2))
    print("h = eps | f'(x)=", dr(f, 2, np.sqrt(eps)))

    print("Diferença central:")
    print("h = 0.01 | f'(x)=", dc(f, 2, h1))
    print("h = 0.001 | f'(x)=", dc(f, 2, h2))
    print("h = eps | f'(x)=", dc(f, 2, eps ** (1 / 3)))

    print("Derivada com SciPy:")
    r = derivative(f, 2)
    print("f'(x)=", r.df)

    fd = lambda x: np.cos(x)
    print("Derivada analítica:")
    print("f'(x) = cos(x)")
    print("f'(x)=", fd(2))

    print("f(x) = e^(-x)")

    f = lambda x: np.exp(-x)

    print("Diferença progressiva:")
    print("h = 0.01 | f'(x)=", dp(f, 1, h1))
    print("h = 0.001 | f'(x)=", dp(f, 1, h2))
    print("h = eps | f'(x)=", dp(f, 1, np.sqrt(eps)))

    print("Diferença regressiva:")
    print("h = 0.01 | f'(x)=", dr(f, 1, h1))
    print("h = 0.001 | f'(x)=", dr(f, 1, h2))
    print("h = eps | f'(x)=", dr(f, 1, np.sqrt(eps)))

    print("Diferença central:")
    print("h = 0.01 | f'(x)=", dc(f, 1, h1))
    print("h = 0.001 | f'(x)=", dc(f, 1, h2))
    print("h = eps | f'(x)=", dc(f, 1, eps ** (1 / 3)))

    print("Derivada com SciPy:")
    r = derivative(f, 1)
    print("f'(x)=", r.df)

    fd = lambda x: -np.exp(-x)
    print("Derivada analítica:")
    print("f'(x) = e^(-x)")
    print("f'(x)=", fd(1))


    #Atividade 2
    print("-- Atividade 2 --")

    vi = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0], dtype = float)
    vo = np.array([0.0, 1.05, 1.83, 2.69, 3.83, 4.56, 5.49, 6.56, 6.11, 7.06, 8.29], dtype = float)

    i1 = np.where(np.isclose(vi, 1.0))[0][0]
    i45 = np.where(np.isclose(vi, 4.5))[0][0]

    a =  lambda i: (vo[i + 1] - vo[i]) / (vi[i + 1] - vi[i])

    b = lambda i: (vo[i] - vo[i - 1]) / (vi[i] - vi[i - 1])

    c = lambda i: (vo[i + 1] - vo[i - 1]) / (vi[i + 1] - vi[i - 1])

    V = np.column_stack((vi, vi**3))
    coeffs, *_ = np.linalg.lstsq(V, vo, rcond = None)
    a1, a3 = coeffs
    d = lambda x: a1 + 3*a3*(x**2)

    print(a(i1), b(i1), c(i1), d(1.0))
    print(a(i45), b(i45), c(i45), d(4.5))


if __name__ == "__main__":
    main()
