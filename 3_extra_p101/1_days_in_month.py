"""
Crea la función days_in_month (month, year) que acepta un número de mes (1-12) y un año, y devuelve la cantidad de días que tiene ese mes. Asegúrate de tener en cuenta si es un año bisiesto para febrero.
"""

def is_leap_year(year):
  if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    result =  True
  else:
    result = False
  return result

def days_in_month(month, year):
  days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month < 1 or month > 12:
    return "Número de mes inválido"

  if month == 2 and is_leap_year(year):
    return 29
  else:
    return days_per_month[month - 1]

print(days_in_month(2,2024))