"""
¿Qué pasa si tu función es llamada con los siguientes números?
1
0
números negativos
1. ¿Es una función parcial o total?
Parcial
2. Ya que estamos, ¿es reversible?
No

Por definición, un número primo es un número entero mayor que 1 que solo es divisible por sí mismo y por 1. Los números negativos no se consideran primos, ya que no cumplen con esta definición.

En matemáticas, los números primos se definen únicamente para valores enteros positivos. Por lo tanto, si intentas verificar si un número negativo es primo, el resultado será falso, ya que no cumple con la definición de un número primo.
"""

def is_prime(numero):
  is_prime = True
  # Agrego esta comprobación
  if numero < 2:
    is_prime = False
  for item in range(2, numero // 2):
    if numero % item == 0:
      is_prime = False
      break
  return is_prime

print(is_prime(1))
print(is_prime(0))
print(is_prime(-2))
print(is_prime(2))
print(is_prime(3))
print(is_prime(11))