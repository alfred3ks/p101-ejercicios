"""
Crea la función all_equal_chars . Recibe una cadena (una secuencia de caracteres) y devuelve
True si todos los caracteres son iguales.
Por ejemplo:
all_equal_chars('aaaaaaaaaaaa') devuelve True all_equal_chars('aaaaaaxaaaaaa')
devuelve False
¿Cual es el caso extremo y qué debe de devolver?
Función total o parcial?
¿Qué tipo de función es?
"""

def all_equal_chars(string):
  is_equal = True
  for i in string:
    if i != string[0]:
      is_equal = False
      break
  return is_equal

print(all_equal_chars('aaaaaa'))
print(all_equal_chars('aaxyaa'))