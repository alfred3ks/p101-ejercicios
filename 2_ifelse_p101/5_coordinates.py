"""
Crea la función classify que recibe las coordenadas de un punto (x, y) en el plano cartesiano.
Devuelve una cadena que indica en qué cuadrante se encuentra el punto ("primer", "segundo", "tercer" o
"cuarto cuadrante") o si está sobre alguno de los ejes ("eje x", "eje y"), o por último, si está en el origen
("origen").
¿Es una función parcial o total?
R: Total
"""

def classify(x, y):
  if x == 0 and y == 0:
    position = "origin"
  elif x == 0:
    position = "y-axis"
  elif y == 0:
    position = "x-axis"
  elif x > 0 and y > 0:
    position = "first quadrant"
  elif x < 0 and y > 0:
    position = "second quadrant"
  elif x < 0 and y < 0:
    position = "third quadrant"
  else:
    position = "fourth quadrant"
  return position

print(classify(0,0))
print(classify(2,-8))
print(classify(2,0))