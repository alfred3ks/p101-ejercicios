"""
Crea la función is_leap que recib eun año y determina si un año es bisiesto.
Un año es bisiesto si es divisible entre 4, excepto aquellos divisibles entre 100 pero no entre 400.
¿Es un predicado?
R: Si ya que devuelve true o false
"""

def is_leap(anio):
  if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
    result =  True
  else:
    result = False
  return result

print(is_leap(1997))
print(is_leap(1998))
print(is_leap(1975))
print(is_leap(1976))