"""
Crea una función bigger que recibe dos números.
Si son iguales, devuelve cualquiera de ellos, sino, devuelve el que sea mayor.
"""

def bigger(a, b):
  if a >= b:
    numero = a
  else:
    numero = b
  return numero

print(bigger(0,0))
print(bigger(10,0))
print(bigger(3,9))
print(bigger('xi','yyu'))

