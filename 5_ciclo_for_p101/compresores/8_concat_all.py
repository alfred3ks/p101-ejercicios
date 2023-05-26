"""
Crea la función concat_all , que recibe una lista de cadenas y devuelve otra cadena, con todas
ellas concatenadas. Asegúrate de que funciona correctamente con la lista vacía.
"""

def concat_all(list_string):
  new_list = ''
  if list_string == []:
    new_list = None
  for string in list_string:
    new_list = new_list + string
  return new_list

print(concat_all([]))
print(concat_all(['Madrid', 'Barcelona', 'Cadiz']))