"""
Crea la función multiplo_de(numero, base) que acepta dos números enteros y devuelve True si el primer número es múltiplo del segundo, y False en caso contrario.
"""

def multiplo_de(numero, base):
  if numero % base == 0:
    message =  True
  else:
    message = False
  return message

print(multiplo_de(8,2))
print(multiplo_de(7,2))