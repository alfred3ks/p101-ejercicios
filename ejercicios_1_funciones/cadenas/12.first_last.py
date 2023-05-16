"""
Crea la función first_last() que acepta una cadena s y devuelve una nueva cadena con el primer y último
caracteres de s.
"""

def first_last(s):
  ci = s[0]
  cf = s[-1]
  result = ci + cf
  return result

print(first_last('Pepito123'))
