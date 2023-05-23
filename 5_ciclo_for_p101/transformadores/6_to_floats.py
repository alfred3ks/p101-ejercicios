"""
Crea la función to_floats que recibe una lista de números y devuelve una nueva lista que contiene esos números convertidos en números decimales ( float ).
Por ejemplo:
[1.01, 8, 42] --> [1.01, 8.0, 42.0]
Recuerda que el tipo de destino es float .
"""

def to_floats(elements):
  new_list = []
  for element in elements:
    number_float = float(element)
    new_list.append(number_float)
  return new_list

print(to_floats([1.01, 8, 42]))