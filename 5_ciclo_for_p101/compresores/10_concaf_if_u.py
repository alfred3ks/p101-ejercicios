"""
Crea la función concat_if_u . Recibe una lista de cadenas y devuelve la concatenación de todas
aquellas que contienen una u.
Recuerda dividir para vencer. ¿Hay algún sub-problema que resolver antes de meter mano al
principal?
"""

def is_string(string):
  is_string = False
  for i in string:
    if i == 'u':
      return True
  return is_string

def concat_if_u(list_string):
  new_list = ''
  for item in list_string:
    if is_string(item):
      new_list += item
  return new_list

print(concat_if_u(['urano', 'marte', 'unico', 'unicornio', 'martes']))
print(concat_if_u(['unico', 'urbanita', 'arco', 'universal', 'viernes']))
