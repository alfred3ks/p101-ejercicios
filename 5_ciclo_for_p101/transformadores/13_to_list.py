"""
Crea la función to_lists que recibe una lista y devuelve otra con cada uno de los elementos de la de entrada convertido en una lista. Es decir, devolverá una lista de listas.
"""

def to_list(elements):
  new_elements = []
  for element in elements:
    sub_list = [element]
    new_elements.append(sub_list)
  return new_elements

print(to_list([1,2,3,4,5,6]))
print(to_list(['a','e','i','o','u']))