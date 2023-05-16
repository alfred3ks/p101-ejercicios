"""
Crea la función calcula_tarifa(edad) que acepta la edad de un visitante y devuelve el precio de la entrada a un evento. Si el visitante es menor de 5 años, la entrada es gratuita; si tiene entre 5 y 18 años, el precio es de 10 dólares; y si tiene 19 años o más, el precio es de 15 dólares.
"""

def calcula_tarifa(edad):
  if edad < 0:
    precio_entrada = 'La edad no puede ser un numero negativo'
  elif edad >= 0 and edad < 5:
    precio_entrada = 'Gratuito'
  elif edad >= 5 and edad <= 18:
    precio_entrada = '10 dolares'
  else:
    precio_entrada = '15 dolares'
  return precio_entrada

print(calcula_tarifa(-4))
print(calcula_tarifa(0))
print(calcula_tarifa(18))
print(calcula_tarifa(19))