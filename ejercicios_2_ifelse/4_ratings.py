"""
Crea una función que recibe la calificación de un estudiante (entre 0 y 100).
Devuelve la clasificación correspondiente: "Sobresaliente" (90-100), "Notable" (80-89), "Aprobado" (65-79) o
"Reprobado" (0-64).
"""

def qualification(note):
  if note >= 90 and note <= 100:
    result = 'Sobresaliente'
  elif note >= 80 and note <= 89:
    result = 'Notable'
  elif note >= 65 and note <= 79:
    result = 'Aprobado'
  elif note >= 0 and note <= 64:
    result = 'Reprobado'
  else:
    result = 'The note is out of range.'
  return result

print(qualification(78))
print(qualification(-5))
print(qualification(32))