"""
#7:
Crea la función round_list que recibe una lista de números (enteros o decimales) y devuelve una lista de decimales redondeados a dos posiciones.
[1.01, 8, 42.009] --> [1.01, 8.00, 42.01]
1. Averigua cómo funciona round de Python
2. Aprovecha la función to_floats
"""

def round_list(elements):
  new_list = []
  for element in elements:
    number = round(float(element),2)
    new_list.append(number)
  return new_list

print(round_list([1.016, 8.023, 42.009]))