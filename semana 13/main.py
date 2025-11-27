import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

from algoritmos import (
    newton,
    lagrange,
    polinomial,
    regressao,
    dp, 
    dr, 
    dc,
    medio,
    trapezio,
    simpson,
    integral,
)

def main() :
    print("-- Segundo Trabalho --")
    print("-- Atividade 1 --")

    x = np.array(
        [1.5, 2.0, 2.2, 3.0]
        , dtype=float
    )

    y = np.array(
        [4.9, 3.3, 3.0, 2.0]
        , dtype=float
    )   

    xr = np.array(
        [1.75, 2.5, 2.75, 3.2]
        , dtype=float
    )

    p = polinomial(x, y)
    yp = np.polyval(p, xr)
    print(yp)


    print("-- Atividade 2 --")

    x = np.array(
        [0.2, 0.5, 0.7, 1.0],
        dtype=float,
    )
    
    y = np.array(
        [0.8187, 1.5815, 1.9354, 2.2905],
        dtype=float,
    )

    xr = np.array(
        [0.3, 0.9],
        dtype=float,
    ) 

    p = polinomial(x, y)
    yp = np.polyval(p, xr)

    print(yp, "A")

    print("-- Atividade 3 --")
    
    x = np.array([1.0, 1.25, 1.5, 1.75, 2.0], dtype=float)
    y = np.array([38.0, 40.0, 42.0, 44.0, 46.0], dtype=float)
    v = lambda x: np.column_stack((np.ones(len(x)), x))

    A = regressao(x, y, v)

    print("Outono:", A)

    x = np.array([1.0, 1.5, 2.0, 2.5, 3.0], dtype=float)
    y = np.array([40.0, 44.0, 48.0, 52.0, 56.0], dtype=float)
    v = lambda x: np.column_stack((np.ones(len(x)), x))

    A = regressao(x, y, v)

    print("Inverno:", A)

    x = np.array([1.0, 1.15, 1.3, 1.45, 1.6], dtype=float)
    y = np.array([36.0, 39.0, 42.0, 45.0, 48.0], dtype=float)
    v = lambda x: np.column_stack((np.ones(len(x)), x))

    A = regressao(x, y, v)

    print("Outono:", A)    
   
    print("-- Atividade 4 --")

    x = np.array([0.5, 1.1, 1.5, 2.2, 2.5, 3.1], dtype=float)
    y = np.array([5.1, 10.3, 15.2, 20.1, 24.7, 30.5], dtype=float)
    v = lambda x: np.column_stack((np.ones(len(x)), x))

    A = regressao(x, y, v)

    print(A)

    print("-- Atividade 5 --")

    R = 5.0
    L = 0.1

    t = np.array([0.0, 0.1, 0.2, 0.3, 0.4], dtype=float)
    I = np.array([0.00, 0.82, 1.36, 1.60, 1.73], dtype=float)

    a, b = np.polyfit(t, I, 1)

    I1 = lambda x: a * x + b

    h = 0.1

    dI = dp(I1, 0.5, h)  
    In = I1(0.5)

    V05 = L * dI + R * In

    print(V05, "V")

    print("-- Atividade 6 --")

    R = 5.0
    L = 0.1

    t = np.array([0.0, 0.1, 0.2, 0.3, 0.4], dtype=float)
    I = np.array([0.00, 0.82, 1.36, 1.60, 1.73], dtype=float)

    a, b, c = np.polyfit(t, I, 2)

    I2 = lambda x: a * x**2 + b * x + c

    h = 0.1

    dI = dr(I2, 0.5, h)  
    In = I2(0.5)

    V05 = L * dI + R * In

    print(V05, "V")

    print("-- Atividade 7 --")
    
    R = 5.0
    L = 0.1

    t = np.array([0.0, 0.1, 0.2, 0.3, 0.4], dtype=float)
    I = np.array([0.00, 0.82, 1.36, 1.60, 1.73], dtype=float)

    a, b, c, d = np.polyfit(t, I, 3)

    I3 = lambda  x: a * x**3 + b * x**2 + c * x + d

    h = 0.1

    dI = dr(I3, 0.5, h)  
    In = I3(0.5)

    V05 = L * dI + R * In

    print(V05, "V")
    
    print("-- Atividade 8 --")

    a = 0
    b = 1.25

    f = lambda x: x * 3 * ((1 - (x/4))**(1/7))
    r = integral(medio, f, a, b)

    Q = 2 * np.pi * r
    print(f"Q(r) = {Q:.8}")


    a = 0
    b = 2.55

    f = lambda x: x * 3 * ((1 - (x/4))**(1/7))
    r = integral(medio, f, a, b)

    Q = 2 * np.pi * r
    print(f"Q(r) = {Q:.8}")

    a = 0
    b = 3.15

    f = lambda x: x * 3 * ((1 - (x/4))**(1/7))
    r = integral(medio, f, a, b)

    Q = 2 * np.pi * r
    print(f"Q(r) = {Q:.8}")

    a = 0
    b = 3.95

    f = lambda x: x * 3 * ((1 - (x/4))**(1/7))
    r = integral(medio, f, a, b)

    Q = 2 * np.pi * r
    print(f"Q(r) = {Q:.8}")

    print("-- Atividade 9 --")

    a = 0
    b = 1.25

    f = lambda x: x * 3 * ((1 - (x/4))**(1/7))
    r = integral(trapezio, f, a, b)

    Q = 2 * np.pi * r
    print(f"Q(r) = {Q:.8}")

    a = 0
    b = 2.55

    f = lambda x: x * 3 * ((1 - (x/4))**(1/7))
    r = integral(trapezio, f, a, b)

    Q = 2 * np.pi * r
    print(f"Q(r) = {Q:.8}")

    a = 0
    b = 3.15

    f = lambda x: x * 3 * ((1 - (x/4))**(1/7))
    r = integral(trapezio, f, a, b)

    Q = 2 * np.pi * r
    print(f"Q(r) = {Q:.8}")

    a = 0
    b = 3.95

    f = lambda x: x * 3 * ((1 - (x/4))**(1/7))
    r = integral(trapezio, f, a, b)

    Q = 2 * np.pi * r
    print(f"Q(r) = {Q:.8}")

    print("-- Atividade 10 --")

    a = 0
    b = 1.25

    f = lambda x: x * 3 * ((1 - (x/4))**(1/7))
    r = integral(simpson, f, a, b)

    Q = 2 * np.pi * r
    print(f"Q(r) = {Q:.8}")

    a = 0
    b = 2.55

    f = lambda x: x * 3 * ((1 - (x/4))**(1/7))
    r = integral(simpson, f, a, b)

    Q = 2 * np.pi * r
    print(f"Q(r) = {Q:.8}")

    a = 0
    b = 3.15

    f = lambda x: x * 3 * ((1 - (x/4))**(1/7))
    r = integral(simpson, f, a, b)

    Q = 2 * np.pi * r
    print(f"Q(r) = {Q:.8}")

    a = 0
    b = 3.95

    f = lambda x: x * 3 * ((1 - (x/4))**(1/7))
    r = integral(simpson, f, a, b)

    Q = 2 * np.pi * r
    print(f"Q(r) = {Q:.8}")


if __name__ == "__main__":
    main()      