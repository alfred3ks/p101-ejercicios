"""
Crea el predicado is_prime(n) que devuelve True si n es un número primo.Hazlo probando todas los posibles divisores de 2 hasta n // 2 .
Cuando la tengas, comprueba con los siguientes números primos:
5
17
29
2161
7919
Cuando compruebes el funcionamiento de un predicado, no pruebes sólo un caso, prueba el otro también. Es decir, comprueba si detecta correctamente números compuestos, como el 1000, 2, 98 ó 21124.
"""

def is_prime(n):
  is_prime = True
  for item in range(2, n // 2):
    if n % item == 0:
      is_prime = False
      break
  return is_prime

# print(is_prime(5))
print(is_prime(17))
# print(is_prime(29))
# print(is_prime(2161))
# print(is_prime(7919))
# print(is_prime(1000))
# print(is_prime(2))
# print(is_prime(98))
# print(is_prime(21124))


# Otra version, sin el n // 2 hace mas comprobaciones.
def is_prime_new(n):
  is_prime = True
  for item in range(2, n):
    if item % n == 0:
      is_prime =  False
      break
  return is_prime

print(is_prime_new(5))
print(is_prime(17))
print(is_prime(21124))