"""
Crea la función make_inverses que recibe una lista de números, y devuelve otra lista de igual longitud con los inversos de cada uno de los números de entrada. Respeta el orden.
"""

def make_inverses(elements):
  inverses_list = []
  for element in elements:
    inverse = 1 / element
    inverses_list.append(inverse)
  return inverses_list

print(make_inverses([1,2,3,4]))