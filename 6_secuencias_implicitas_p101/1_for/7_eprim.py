"""
Un eprim (prime al revés) es un primo que al invertir sus dígitos, también te da otro primo.
Por ejemplo, 13:
13, 31 son ambos primos
Crea el predicado eprim(n) que recibe un número y devuelve si es un eprim.
Pistas:
1. Divide y vencerás: ya tienes una función que decide si un número es primo o no y otra que invierte secuencias.
2. Para convertir un tipo a otro, se usa el tipo de destino como una función. Por ejemplo, para convertir un número en una cadena, se haría str(986) . Para convertir una cadena en un número se haría int("98").
"""

def is_prime(n):
  m = int(n)
  is_prime = True
  if m < 2:
    is_prime = False
  for item in range(2, m // 2):
    if m % item == 0:
      is_prime = False
      break
  return is_prime

def rev(n):
  # Transformo si entra una cadena a numero
  reverse = int(str(n)[::-1])
  return reverse

def eprim(n):
  are_prime = False
  if is_prime(n) and is_prime(rev(n)):
    are_prime = True
  return are_prime

print(eprim(13))
print(eprim(17))
print(eprim('98'))
print(eprim(41))
print(eprim(73))

