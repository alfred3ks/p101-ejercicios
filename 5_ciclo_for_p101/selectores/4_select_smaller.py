"""
Crea la función select_smaller que recibe 2 parámetros:
1. Un número
2. Una lista de números
devuelve una lista con aquellos que son menores que el parámetro numérico.
Recuerda preservar el orden
¿Qué devolverías si recibes una lista vacía?
¿En qué se distingue de select_bigger ?
"""

def select_smaller(number, elements):
  numbers = []
  for element in elements:
    if element < number:
      numbers.append(element)
  return numbers

print(select_smaller(3, [3,5,78,2,5,1,3,67]))