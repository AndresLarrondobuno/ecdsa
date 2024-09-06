import math
from sha256.obtenerHash import generate_hash

class ECPOINT:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    
    def __str__(self) -> str:
        return f'\n x: {hex(int(self.x))} \n y: {hex(int(self.y))}'

    _A = 0
    _B = 7
    _P = int('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F', 16)
    _N = int('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141', 16)
    _G = None
    
        
    @staticmethod
    def add(a: 'ECPOINT', b: 'ECPOINT') -> 'ECPOINT':
        if (a.x == b.x): return ECPOINT.double(a)
        P = ECPOINT._P
        s = (b.y + P - a.y) * ECPOINT.multiplicativo_inverso_P(b.x + P - a.x) % P
        x = ( math.pow(s, 2) + P - a.x + P - b.x ) % P
        y = ( s * (P + a.x - x) + P - a.y ) % P
        return ECPOINT(x, y)

 
    @staticmethod
    def double(a: 'ECPOINT') -> 'ECPOINT':
        P = ECPOINT._P
        A = ECPOINT._A
        s = (3 * math.pow(a.x, 2) + A) * ECPOINT.multiplicativo_inverso_P(2 * a.y) % P
        x = ( math.pow(s, 2) + P - a.x + P - a.x ) % P
        y = ( s * (P + a.x - x) + P - a.y ) % P
        return ECPOINT(x, y)
    
    
    @staticmethod
    def multiply(k: int, a: 'ECPOINT' = None) -> 'ECPOINT':
        a = a if a != None else ECPOINT.G()
        punto_actual = a
        string_binario = ECPOINT.to_binary_string(k)
        
        for c in string_binario:
            punto_actual = ECPOINT.double(punto_actual)
            if c == '1':
                punto_actual = ECPOINT.add(punto_actual, a)
        return punto_actual
    

    @staticmethod
    def G():
        if ECPOINT._G is None:
            x = int('79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798', 16)
            y = int('483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8', 16)
        return ECPOINT(x, y)
    
    
    @staticmethod
    def to_binary_string(n):
        """Convierte un número entero a su representación binaria en forma de cadena.

        Args:
            n: El número entero a convertir.

        Returns:
            Una cadena con la representación binaria del número.
        """
        return bin(n)[2:]  #elimina el prefijo '0b'
    
    
    @staticmethod
    def multiplicativo_inverso_P(n):
        return ECPOINT.multiplicativo_inverso(n, ECPOINT._P)
    
    
    @staticmethod
    def multiplicativo_inverso_N(n) -> 'ECPOINT':
        return ECPOINT.multiplicativo_inverso(n, ECPOINT._N)
    
    
    @staticmethod
    def algoritmo_extendido_euclideano(a, b):
        if a == 0:
            return b, 0, 1
        else:
            mcd, x, y = ECPOINT.algoritmo_extendido_euclideano(b % a, a)
            return mcd, y - (b // a) * x, x
    
    
    @staticmethod
    def multiplicativo_inverso(n, mod):
        mcd, x, y = ECPOINT.algoritmo_extendido_euclideano(n, mod)
        return x + mod
    
    
    @staticmethod
    def generate_hash(mensaje: bytearray):
        return generate_hash(mensaje)
    
    
    @staticmethod
    def firmar_mensaje(mensaje: bytearray, privateKey: int):
        k = 12345 #debe ser aleatorio
        z = ECPOINT.generate_hash(mensaje)
        R = ECPOINT.multiply(k)
        if R.x == 0: return ECPOINT.firmar_mensaje(mensaje, privateKey)
        s = ECPOINT.multiplicativo_inverso_N(k) * (z + R.x * privateKey) % ECPOINT._N
        return ECPOINT(R.x, s)
    
    #falta funcion de verificacion