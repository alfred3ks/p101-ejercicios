# Ejercicio 4
# función que calcula de octavos de milla a metros, recibe los octavos y retorna los metros
import math
def eighth_mile(eighth_mile):
  """
  Calcula en metros octava de millas
  """
  mile = 1609.344
  meters = round( mile * eighth_mile )
  return meters

print(eighth_mile(3))