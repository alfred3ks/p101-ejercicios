"""
La fórmula para el área de una esfera es la siguiente:
1. Crea una función que calcula el area de la esfera
2. Usa el de math
area = 4 * PI * radio**2
"""
import math
def sphere_area(radio):
  """
  Calcula el area de una esfera
  """
  area = 4 * math.pi * radio**2
  return area

print(sphere_area(3))