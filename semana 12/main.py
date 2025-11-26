import numpy as np
from scipy.integrate import quad

from algoritmos import (
    medio,
    trapezio,
    simpson,
    integral,
)


def main():
    # Atividade 1
    print("-- Atividade 1 --")

    a = 0
    b = 1
    n = 1e-3

    print("f(x) = e^(-x)")
    f = lambda x: np.exp(-x)
    r = integral(medio, f, a, b, n)
    print(f"Ponto medio = {r:.8}")
    r = integral(trapezio, f, a, b, n)
    print(f"Trapezio = {r:.8}")
    r = integral(simpson, f, a, b, n)
    print(f"Simpson = {r:.8}")
    r, error = quad(lambda x: float(f(x)), a, b)
    print(f"SciPy = {r:.8}")

    print("f(x) =  xˆ2")
    f = lambda x: x**2
    r = integral(medio, f, a, b, n)
    print(f"Ponto medio = {r:.8}")
    r = integral(trapezio, f, a, b, n)
    print(f"Trapezio = {r:.8}")
    r = integral(simpson, f, a, b, n)
    print(f"Simpson = {r:.8}")
    r, error = quad(lambda x: float(f(x)), a, b)
    print(f"SciPy = {r:.8}")

    print("f(x) = xˆ3")
    f = lambda x: x**3
    r = integral(medio, f, a, b, n)
    print(f"Ponto medio = {r:.8}")
    r = integral(trapezio, f, a, b, n)
    print(f"Trapezio = {r:.8}")
    r = integral(simpson, f, a, b, n)
    print(f"Simpson = {r:.8}")
    r, error = quad(lambda x: float(f(x)), a, b)
    print(f"SciPy = {r:.8}")

    print("f(x) = x*np.exp(-x**2)")
    f = lambda x: x*np.exp(-x**2)
    r = integral(medio, f, a, b, n)
    print(f"Ponto medio = {r:.8}")
    r = integral(trapezio, f, a, b, n)
    print(f"Trapezio = {r:.8}")
    r = integral(simpson, f, a, b, n)
    print(f"Simpson = {r:.8}")
    r, error = quad(lambda x: float(f(x)), a, b)
    print(f"SciPy = {r:.8}")

    print("f(x) = 1/(x**2 + 1)")
    f = lambda x: 1/(x**2 + 1)
    r = integral(medio, f, a, b, n)
    print(f"Ponto medio = {r:.8}")
    r = integral(trapezio, f, a, b, n)
    print(f"Trapezio = {r:.8}")
    r = integral(simpson, f, a, b, n)
    print(f"Simpson = {r:.8}")
    r, error = quad(lambda x: float(f(x)), a, b)
    print(f"SciPy = {r:.8}")

    print("f(x) = x/(x**2 + 1)")
    f = lambda x: x/(x**2 + 1)
    r = integral(medio, f, a, b, n)
    print(f"Ponto medio = {r:.8}")
    r = integral(trapezio, f, a, b, n)
    print(f"Trapezio = {r:.8}")
    r = integral(simpson, f, a, b, n)
    print(f"Simpson = {r:.8}")
    r, error = quad(lambda x: float(f(x)), a, b)
    print(f"SciPy = {r:.8}")


    #Atividade 2
    print("Atividade 2")

    a = 2
    b = 5
    ns = [3, 5, 7, 9]

    print("f(x) = e^(4 - x**2)")

    for n in ns:
        
        f = lambda x: np.exp(4 - x**2)
        r = integral(medio, f, a, b, n)
        print(f"Ponto medio = {r:.7}")
        r = integral(trapezio, f, a, b, n)
        print(f"Trapezio = {r:.7}")
        r = integral(simpson, f, a, b, n+1)
        print(f"Simpson = {r:.7}")


if __name__ == "__main__":
    main()
