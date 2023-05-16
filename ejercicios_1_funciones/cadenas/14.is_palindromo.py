"""
Crea la función is_palindromo(s) que acepta una cadena s y devuelve True si s es un palíndromo (se lee
igual hacia adelante y hacia atrás) y False si no lo es. Usa la función anterior.
"""

def reverse(s):
  result = s[::-1]
  return result

def is_palindromo(s):
  new_s = s.lower().replace(' ', '')
  is_palindromo_s = new_s == reverse(new_s)
  return is_palindromo_s

print(is_palindromo('amor a roma'))
print(is_palindromo('amor'))
print(is_palindromo('Was it a car or a cat I saw'))