"""
Crea la función count_str que recibe una lista y devuelve el número de cadenas que hay en ella.
Asegúrate de que funciona cuando:
- solo hay cadenas
- no hay ninguna cadena
- la lista de entrada es la vacía
1. ¿Se parece en algo a sum_mult_of_3 ?
Si se parecen ambas funciones dependen su resultado del predicado, de devolver True.
"""

caracter_list = ['hola', 'mundo', 'feliz', 'madrid']
# caracter_list = []
# caracter_list = [2,45,67]

def count_str(caracter_list):
  count = 0
  for element in caracter_list:
    if type(element) == str:
      count += 1
  return count

print(count_str(caracter_list))


# Otra opcion:
def count_str_a(caracter_list):
  count = 0
  for element in caracter_list:
    if isinstance(element, str):
      count += 1
  return count

print(count_str_a(caracter_list))