"""
Cuando era niño, los adultos tenían la curiosa afición de atormentar a los niños con juegos idiotas como el siguiente:
1. Le dices al niño: Érase una vez un pez. ¿Quieres que te lo cuente otra vez?
2. Si el niño contesta no, le dices: No te he dicho que no. He dicho: érase una vez un pez.
¿Quieres que te lo cuente otra vez?
3. El bucle persiste hasta que el niño contesta: Erase una vez un pez
Usando esa descripción, la plantilla de bucle potencialmente infinito y la función input crea la función pez() que atormenta al usuario hasta que contesta "Erase una vez un pez".
"""

def pez():
  # imprimo la pregunta
  # Pido la respuesta al usuario
  response = input('Erase una vez un pez. ¿Quieres que te lo cuente otra vez? ')
  while True:
    #Si es la que quiero salgo del bucle
    if response == 'Erase una vez un pez':
      break
    else:
      response = input('No te he dicho que ' + response + ' He dicho: Erase una vez un pez ¿Quieres que te lo cuente otra vez? ')
  #sino repito la pregunta incluyendo la respuesta del usuario

pez()