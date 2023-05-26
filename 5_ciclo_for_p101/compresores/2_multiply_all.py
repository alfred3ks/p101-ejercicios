"""
Siguiendo el método de arriba, crea la función multiply_all , que recibe una lista de números y
devuelve el producto de todos ellos.
"""

def multiply_all(numbers):
  """
  Recibe una lista de numeros y devuelve su producto
  Si recibe la lista vacia devuelve 0
  Si recibe una lista que no son numeros, palma
  Devuelve 1 para una lista vacia porque es el valor neutro del producto, el de la suma es cero.
  """
  total_number = 1
  for number in numbers:
    total_number = total_number * number
  return total_number

print(multiply_all([1,2,3,4,5,6,7]))