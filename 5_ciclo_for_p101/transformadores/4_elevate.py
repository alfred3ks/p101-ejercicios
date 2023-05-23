"""
Crea una función llamada elevate que recibe dos parámetros:
- una lista de números
- un número llamado exponent
Devuelve una nueva lista, con el resultado de elevar cada uno de los elementos originales a exponent
"""

def elevate(numbers, exp):
  new_list = []
  for number in numbers:
    number_elevate = number**exp
    new_list.append(number_elevate)
  return new_list

print(elevate([1,2,3,4], 3))