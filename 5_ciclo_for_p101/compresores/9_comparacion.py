"""
Compara concat_all con sum_all . ¿En qué se parecen? ¿En qué se distinguen? ¿Ves algún
patrón?
R: Pues si ambas funciones son muy parecedas, una convierte una lista de numeros a un numero y la otra una lista de cadenas a una sola cadena.
"""

def sum_all(numbers):
  total_number = 0
  for number in numbers:
    total_number = total_number + number
  return total_number

print(sum_all([1,2,3,4,5,6,7]))

def concat_all(list_string):
  new_list = ''
  if list_string == []:
    new_list = None
  for string in list_string:
    new_list = new_list + string
  return new_list

print(concat_all([]))
print(concat_all(['Madrid', 'Barcelona', 'Cadiz']))