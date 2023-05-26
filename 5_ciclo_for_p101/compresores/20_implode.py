"""
Crea la función implode . Recibe una lista de cadenas y la convierte en una cadena,
concatenando todo y respetando el orden.
1. ¿ implode es una función reversible?
"""

def implode(list_string):
  new_list = ''
  if list_string == []:
    new_list = None
  for string in list_string:
    new_list = new_list + string
  return new_list

print(implode([]))
print(implode(['Madrid', 'Barcelona', 'Cadiz']))
