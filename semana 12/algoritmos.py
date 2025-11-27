# algoritmos.py
def medio(f, a, b):
    h = b - a
    return h * f((a + b) / 2)

def trapezio(f, a, b):
    h = b - a
    return h * (0.5 * f(a) + 0.5 * f(b))

def simpson(f, a, b):
    h = (b - a) / 2
    return h * ((1/3) * f(a) + (4/3) * f((a + b) / 2) + (1/3) * f(b))

def integral(metodo, f, a, b, n):
    s = 0.0
    c = a
    d = a + n
    while d <= b + 1e-15:
        s += metodo(f, c, d)
        c = d
        d += n
    return s

# ---- MÉTODOS COMPOSTOS ----
def medio_composto(f, a, b, n):
    h = (b - a) / n
    s = 0.0
    for i in range(n):
        x_m = a + (i + 0.5) * h
        s += f(x_m)
    return s * h

def trapezio_composto(f, a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x = a + i * h
        s += f(x)
    return s * h

def simpson_composto(f, a, b, n):

    if n % 2 != 0:
        raise ValueError("número par")
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            s += 2 * f(x)
        else:
            s += 4 * f(x)
    return s * h / 3

def integral_composto(metodo_simples, f, a, b, n):
    h = (b - a) / n
    s = 0.0
    c = a
    for _ in range(n):
        d = c + h
        s += metodo_simples(f, c, d)
        c = d
    return s