"""
Funcion de transformacion tema nuevo:
#1:
Construye una función llamada make_lengths que recibe una lista de cadenas y devuelve: una lista de
números , de la misma longitud de la lista de entrada. Cada uno de esos números es la longitud de cada una
de las cadenas de entrada.
Por ejemplo:
["hey", "hola", "mundo"] --> [3, 4, 5] [] --> []
"""

def make_lengths(elements):
  result = []
  for element in elements:
    result.append(len(element))
  return result

print(make_lengths(["hey", "hola", "mundo"]))
print(make_lengths([]))