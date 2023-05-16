"""
Crea la función puntuacion_juego(puntuacion) que acepta la puntuación en un juego y devuelve una cadena que indica el rango de puntuación: "Principiante" (0-500), "Intermedio" (501-2000) o "Experto" (más de 2000).
"""

def puntuacion_juego(puntuacion):
  if puntuacion < 0:
    result = 'El valor esta fuera de rango'
  elif puntuacion >= 0 and puntuacion <= 500:
    result = 'Principiante'
  elif puntuacion >= 501 and puntuacion <= 2000:
    result = 'Intermedio'
  else:
    result = 'Experto'
  return result

print(puntuacion_juego(-2))
print(puntuacion_juego(344))
print(puntuacion_juego(612))
print(puntuacion_juego(2001))