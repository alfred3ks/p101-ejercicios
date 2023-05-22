"""
#3
Crea la función select_bigger que recibe 2 parámetros:
1. Un número
2. Una lista de números devuelve una lista con aquellos que son mayores que el parámetro numérico.
Recuerda preservar el orden
"""
def select_bigger(number, elements):
  numbers = []
  for element in elements:
    if element > number:
      numbers.append(element)
  return numbers

print(select_bigger(3, [3,5,78,2,5,2,3,67]))