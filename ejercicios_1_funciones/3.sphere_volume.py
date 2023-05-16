# Ejercicio 3
# Volumen de una esfera
# volumen = (pi + radio**3) / 3
import math
def sphere_volume(radio):
  """
  Calcula el volumen de una esfera
  """
  volumen = (math.pi * radio**3) / 3
  return volumen

print(sphere_volume(3))