import numpy as np
import matplotlib.pyplot as plt

from algoritmos import bissecao
from algoritmos import seidel
from algoritmos import  (
    G, 
    GN, 
    fixed_point)


# Função Atividade1
def f1(T):
    K = 272.975 # Temperatura (K)
    E = 500.125
    return 5.67e-8 * (T**4) + 0.4 * (T - K) - E

def main():
    #1° Trabalho
    print("-- Trabalho 1 --")

    # Atividade 1
    print("-- Atividade 1 --")
    r, i = bissecao(f1, 300, 320, 1e-5)
    print(f"raiz = {r} , i = {i}")

    # Atividade 2
    print("-- Atividade 2 --")
    A = np.array([[17, -2, -3], [-5, 21, -2], [-5, -5, 22]], dtype=float)
    B = np.array([500, 200, 300], dtype=float)
    print("\nMatriz A:")
    print(A)
    print("\nVetor B:")
    print(B)
    print("\nSolução Seidel x:")
    X = seidel(A, B, 100, 1e-8)
    print(X)

    #Atividade 3
    print("-- Atividade 3 --")
    A = np.array([[20, 10], [10, 20]], dtype = float)
    B = np.array([100, 100], dtype = float)
    print("\nMatriz A:")
    print(A)
    print("\nVetor B:")
    print(B)
    print("\nSolução Seidel x:")
    X = seidel(A, B, 100, 1e-8)
    print(X)
    print("Corrente no resistor R3")
    I3 = np.sum(X)
    print(I3, "A")

    #Atividade 4

    print("-- Atividade 4 --")
    def F(x):
        x1, x2 = x
        return np.array([
            (x1**4 + 0.06823*x1) - (x2**4 + 0.05848*x2) - 0.01753,
            (x1**4 + 0.05848*x1) - (2*x2**4 + 0.11696*x2) -  0.00254       
        ], dtype = float)

    x = np.array([0.0, 0.0], dtype=float) 
    r = fixed_point(x, lambda x: GN(x, F))
    print(r)   

if __name__ == "__main__":
    main()