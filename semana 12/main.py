# main.py
import numpy as np
from scipy.integrate import quad
from algoritmos import (
    medio,
    trapezio,
    simpson,
    integral,
    medio_composto,
    trapezio_composto,
    simpson_composto,
    integral_composto,
)

def main():
    print("-- Atividade 1 --")
    a = 0.0
    b = 1.0
    c = 1e-3   

    print("f(x) = e^(-x)")
    f = lambda x: np.exp(-x)
    r = integral(medio, f, a, b, c)
    print(f"Ponto medio = {r:.8}")
    r = integral(trapezio, f, a, b, c)
    print(f"Trapezio = {r:.8}")
    r = integral(simpson, f, a, b, c)
    print(f"Simpson = {r:.8}")
    r, error = quad(lambda x: float(f(x)), a, b)
    print(f"SciPy = {r:.8}\n")

    
    print("f(x) = x^2")
    f = lambda x: x**2
    r = integral(medio, f, a, b, c)
    print(f"Ponto medio = {r:.8}")
    r = integral(trapezio, f, a, b, c)
    print(f"Trapezio = {r:.8}")
    r = integral(simpson, f, a, b,c)
    print(f"Simpson = {r:.8}")
    r, error = quad(lambda x: float(f(x)), a, b)
    print(f"SciPy = {r:.8}\n")

    
    print("f(x) = x^3")
    f = lambda x: x**3
    r = integral(medio, f, a, b, c)
    print(f"Ponto medio = {r:.8}")
    r = integral(trapezio, f, a, b, c)
    print(f"Trapezio = {r:.8}")
    r = integral(simpson, f, a, b, c)
    print(f"Simpson = {r:.8}")
    r, error = quad(lambda x: float(f(x)), a, b)
    print(f"SciPy = {r:.8}\n")

    
    print("f(x) = x * exp(-x^2)")
    f = lambda x: x * np.exp(-x**2)
    r = integral(medio, f, a, b, c)
    print(f"Ponto medio = {r:.8}")
    r = integral(trapezio, f, a, b, c)
    print(f"Trapezio = {r:.8}")
    r = integral(simpson, f, a, b, c)
    print(f"Simpson = {r:.8}")
    r, error = quad(lambda x: float(f(x)), a, b)
    print(f"SciPy = {r:.8}\n")

    
    print("f(x) = 1/(1 + x^2)")
    f = lambda x: 1.0 / (1.0 + x**2)
    r = integral(medio, f, a, b, c)
    print(f"Ponto medio = {r:.8}")
    r = integral(trapezio, f, a, b, c)
    print(f"Trapezio = {r:.8}")
    r = integral(simpson, f, a, b, c)
    print(f"Simpson = {r:.8}")
    r, error = quad(lambda x: float(f(x)), a, b)
    print(f"SciPy = {r:.8}\n")

    
    print("f(x) = x / (1 + x^2)")
    f = lambda x: x / (1.0 + x**2)
    r = integral(medio, f, a, b, c)
    print(f"Ponto medio = {r:.8}")
    r = integral(trapezio, f, a, b, c)
    print(f"Trapezio = {r:.8}")
    r = integral(simpson, f, a, b, c)
    print(f"Simpson = {r:.8}")
    r, error = quad(lambda x: float(f(x)), a, b)
    print(f"SciPy = {r:.8}\n")


    print("-- Atividade 2 --")
    f = lambda x: np.exp(4.0 - x**2)
    a = 2.0
    b = 5.0
    ns = [3, 5, 7, 9]

    for n in ns:
        print(f"n = {n}")
        r = medio_composto(f, a, b, n)
        print(f"Ponto medio = {r:.7f}")

        r = trapezio_composto(f, a, b, n)
        print(f"Trapezio = {r:.7f}")

        if n % 2 != 0:
            try:
                r = simpson_composto(f, a, b, n)
            except ValueError as e:
                r = simpson_composto(f, a, b, n+1)
        else:
            r = simpson_composto(f, a, b, n)
        print(f"Simpson = {r:.7f}")
        print()

if __name__ == "__main__":
    main()