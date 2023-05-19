# Ejercicio 5
# 1. Crea una función que recibe tu año de nacimiento y calcula tu edad en años

def age(year):
  """
  Calcula la edad a partir del año de nacimiento
  """
  current = 2023
  age = current - year
  return age

print(age(1975))

# 2. Crea una función que hace lo mismo pero te devuelve la edad en días (olvídate de los años bisiestos)
def days(year):
  """
  Calcula los dias a partir del año de nacimiento
  """
  age_in_days = age(year) * 365
  return age_in_days

print(days(2006))