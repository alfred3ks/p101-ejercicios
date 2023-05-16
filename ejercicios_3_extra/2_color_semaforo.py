"""
Crea la función color_semaforo(color) que acepta el color de la luz en un semáforo (rojo, amarillo o verde) y
devuelve una cadena que indica qué acción debe tomar un conductor: detenerse, precaución o avanzar.
"""

def color_semaforo(color):
  if color == 'rojo':
    message = 'detenerse'
  elif color == 'amarillo':
    message = 'precaucion'
  elif color == 'verde':
    message = 'avanzar'
  else:
    message= 'The color you have entered is not correct'
  return message

print(color_semaforo('verde'))
print(color_semaforo('amarillo'))
print(color_semaforo('rojo'))
print(color_semaforo('orange'))