def algoritmo_extendido_euclideano(a, b):
    if a == 0:
        return b, 0, 1
    else:
        mcd, x, y = algoritmo_extendido_euclideano(b % a, a)
        return mcd, y - (b // a) * x, x
    

def obtener_multiplicativo_inverso(n, mod):
    mcd, x, y = algoritmo_extendido_euclideano(n, mod)
    return x + mod

n = 13
mod = 37

multiplicativo_inverso = obtener_multiplicativo_inverso(n, mod)
print(f'Inverso multiplicativo modular: {multiplicativo_inverso}')