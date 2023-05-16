"""
Función que recibe una edad y la clasifica de la siguiene manera:
"Infancia" (0-12 años),
"Adolescencia" (13-17 años),
"Jueventud" (18-29 años),
"Adultez" (30-59 años)
"Vejez" (60+ años)
Preguntas:
¿Es una función parcial o total?
R:Parcial ya que no maneja todos los casos de entrada. (negativos)
¿Es un predicado?
R: No, ya que no devuelve true or false
"""

def age_classification(age):
  if age >= 0 and age <= 12:
    classification = 'Infancia'
  elif age >= 13 and age <= 17:
    classification = 'Adolescencia'
  elif age >= 18 and age <= 29:
    classification = 'Juventud'
  elif age >= 30 and age <= 59:
    classification = 'Adultez'
  else:
    classification = 'Vejez'
  return classification

print(age_classification(70))
print(age_classification(-8))