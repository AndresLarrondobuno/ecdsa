from pycoin.ecdsa.secp256k1 import secp256k1_generator

x1 = 3
y1 = 6
x2 = -2
y2 = 2  # Ajusta este valor para que el punto esté en la curva

punto_uno = punto_aleatorio = secp256k1_generator.generate_random_point()
punto_dos = punto_aleatorio = secp256k1_generator.generate_random_point()

punto_tres = punto_uno + punto_dos
print(punto_uno, punto_dos)
print(punto_tres.x, punto_tres.y)