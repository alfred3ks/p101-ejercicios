# Ejercicio 6
# 1. crea la función bmi que recibe peso y altura (en Kg y m)
# 2. devuelve el bmi
# La formula es bmi = peso / altura**2

def bmi( weight, height ):
  """
  Calcula el índice de masa corporal a partir de su altura en mts y peso en Kg
  """
  bmi = round(weight / height**2 , 2)
  return bmi

print(bmi(75, 1.75))