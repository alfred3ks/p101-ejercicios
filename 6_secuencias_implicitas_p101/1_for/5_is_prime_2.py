"""
Si tu función furula como es debido, compárala con ésta:
  def is_prime_2(n):
    is_prime = True
    for number in range(2, n // 2):
      is_prime = (number % 2 == 0)
      if not is_prime:
        break
    return is_prime

1. is_prime_2 ¿está bien o mal?
2. En caso de estar mal, ¿qué está mal y cómo la arreglarías?

La línea is_prime = (number % 2 == 0) está verificando si number es divisible por 2 en lugar de verificar si n es divisible por number. Esto provocará que is_prime se establezca en False si number es par, lo cual no es correcto.

El bucle for debería iterar desde 2 hasta n // 2 + 1 en lugar de n // 2. De lo contrario, se perderán los números que dividen a n correctamente.

La verificación de if not is_prime y la instrucción break deberían estar fuera del bucle for. Actualmente, se romperá el bucle en la primera iteración si is_prime es False, lo cual no es lo que se desea.
"""

def is_prime_2(n):
  is_prime = True
  for number in range(2, n // 2):
    is_prime = (number % 2 == 0)
    if not is_prime:
      break
  return is_prime

# print(is_prime_2(5))
# print(is_prime_2(17))
# print(is_prime_2(29))
# print(is_prime_2(2161))
# print(is_prime_2(7919))
# print(is_prime_2(1000))
# print(is_prime_2(2))
# print(is_prime_2(98))
# print(is_prime_2(21124))

def is_prime_3(n):
  is_prime = True
  for item in range(2, n // 2):
    if n % item == 0:
      is_prime = False
      break
  return is_prime

# print(is_prime_3(5))
print(is_prime_3(17))
# print(is_prime_3(29))
# print(is_prime_3(2161))
# print(is_prime_3(7919))
# print(is_prime_3(1000))
# print(is_prime_3(2))
# print(is_prime_3(98))
# print(is_prime_3(21124))
