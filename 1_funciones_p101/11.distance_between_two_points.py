"""
Si tenemos dos puntos:
Su distancia cartesiana sería la siguiente:
p1(x1,y1)
p2(x2,y2)

La formula para calcular la distancia cartesiana seria:

dc = raiz_cuadrada((x1 - x2)**2 + (y1 - y2)**2)

1. Crear una función que recibe la x e y del primer punto y la x e y del segundo punto.
2. Devuelve la distancia cartesiana.
"""

import math
def distance_between_two_point(x1,y1,x2,y2):
  dc = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
  return dc

print(distance_between_two_point(-1, 2, 1, 2))


# Aqui vemos otra forma sin usar math
def distancia_cartesiana(x1, y1, x2, y2):
  distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
  return distancia

distancia = distancia_cartesiana(-1, 2, 1, 2)
print(distancia)