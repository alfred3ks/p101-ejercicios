"""
Crea la función to_strings que recibe una lista de números y devuelve una nueva lista que contiene esos números convertidos en cadenas: 3 --> "3".
Para la conversión de int o float a str se usa el tipo de destino (en este caso str ) y se le llama como si fuese una función. Por ejemplo: str(8) .
"""

def to_string(numbers):
  new_list_string = []
  for number in numbers:
    string = str(number)
    new_list_string.append(string)
  return new_list_string

print(to_string([1,2,3,4]))