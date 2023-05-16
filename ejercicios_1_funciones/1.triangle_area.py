# Ejercicio 1
# Area de un triángulo
"""
Crea una función que:
recibe los 3 lados
usa la función sqrt que está en math
devuelve el area
La formula para calcula el semiperimetro es:
sp =(lado1 + lado2 + lado3) / 2

El volumen se calcula:
(sp * (sp - side1) * (sp - side2) * (sp - side3))

"""
import math
def triangle_area(side1, side2, side3):
  """
  Calcula el area usando el semi-perímetro
  """
  sp = (side1 + side2 + side3) / 2
  area = math.sqrt(sp * (sp - side1) * (sp - side2) * (sp - side3))
  return area

print(triangle_area(3, 2, 3))
