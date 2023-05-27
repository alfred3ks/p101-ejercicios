"""
Otro juego irritante parecido es El cuento de la buena pipa:
- ¿Quieres que te cuente el cuento de la buena pipa?
- Siiiiiiii - contesta el niño alegremente
- No, no te he dicho «siiiiii», te he dicho «¿Quieres que te cuente el cuento de la buena pipa?»
- Mmmm, pues no
- contesta el niño mirando al cuentista con desconfianza
- No, no te he dicho
«Mmmm, pues no», te he dicho «¿Quieres que te cuente el cuento de la buena pipa?
- Grrrrrrrrrrrrrr
- niño se da por vencido
- No, no te he dicho «Grrrrrrrrrrrrr» …
Vamos a crear la función pipa que implementa esa forma de tortura infantil. No pararemos
hasta que el usuario conteste: ¿Quieres que te cuente el cuento de la buena pipa?
Como en este caso aparece puntuación, vamos a ampliar la función de normalización para que
además de quitar espacios en blanco, y pasar a minúsculas y eliminar caracteres acentuados,
que también elimine los signos de puntuación.
Primero, implementa la función remove_punctuation .
"""
import unicodedata

# Función que remueve los acentos:
def remove_accents(string):
  forma_nfkd = unicodedata.normalize('NFKD', string)
  solo_ascii = forma_nfkd.encode('ASCII', 'ignore')
  return solo_ascii.decode()

# Función de remover acentos:
def remove_punctuation(string):
  index = 0
  clean = ''
  while index < len(string):
    current = string[index]
    if current not in '.,;:¡!¿?':
      clean = clean + current
    index += 1
  return clean

# Función que llama al programa:
def pipa():
  response = input('¿Quieres que te cuente el cuento de la buena pipa? ')
  while True:
    normalize_response = remove_accents(response).strip().lower()
    normalize_response = remove_punctuation(normalize_response)

    if normalize_response == 'quieres que te cuente el cuento de la buena pipa':
      break
    else:
      response = input('No te he dicho que: '+ response + ', He dicho: ¿Quieres que te cuente el cuento de la buena pipa? ')

pipa()