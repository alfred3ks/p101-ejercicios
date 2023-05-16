"""
¿Recuerdas la función bmi que recibia una altura y peso y te devolvía un índice?
Crea la función classify_bmi que recib eun bmi y devuelve una cadena indicando en qué rango está:
"Delgado" : bmi < 18.5
"Saludable": 18.5 < bmi < 24.9
"Gordito" : 25 a 29.9
"Gordo" : 30 a 34.9
"Obeso" : 35 a 39.9
"Jabba the Hutt" : más de 40
"""

def classify_bmi(bmi):
  if bmi < 18.5:
    result = 'Delgado'
  elif bmi > 18.5 and bmi < 24.9:
    result = 'Saludable'
  elif bmi > 25 and bmi < 29:
    result = 'Gordito'
  elif bmi > 30 and bmi < 34.9:
    result = 'Gordo'
  elif bmi > 35 and bmi < 39.9:
    result = 'Obeso'
  elif bmi > 40:
    result = 'Jabba the Hutt'
  return result

print(classify_bmi(19))