"""
Escribe la función sum_all que recibe una lista de números y devuelve la suma total.
En este ejercicio, veremos el proceso general que hay que seguir y los demás los harás tú sólo.
"""

numbers = [1,2,3,4,5,6,7]

def sum_all(numbers):
  """
  Recibe una lista de numeros y devuelve la suma total
  Si recibe la lista vacia devuelve 0
  Si recibe una lista que no son numeros, palma
  """
  # Creamos una variable para el total
  total_number = 0
  # Por cada elemento de la lista
  for number in numbers:
    # lo sumo al total parcial
    total_number = total_number + number
  # Cuando haya terminado, el total parcial, sera
  # El total absoluto y lo devuelvo
  return total_number

print(sum_all(numbers))