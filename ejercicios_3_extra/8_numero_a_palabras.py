"""
Crea la función numero_a_palabras(numero) que acepta un número entero entre 1 y 10 y devuelve una cadena con el número en palabras (por ejemplo, "uno", "dos",etc.). Si el número está fuera del rango, devuelve "Número fuera de rango".
"""
def numero_a_palabras(numero):
  if numero < 1 or numero > 10:
    mensaje = ' Número fuera de rango'
  elif numero == 1:
    mensaje = 'uno'
  elif numero == 2:
    mensaje = 'dos'
  elif numero == 3:
    mensaje = 'tres'
  elif numero == 4:
    mensaje = 'cuatro'
  elif numero == 5:
    mensaje = 'cinco'
  elif numero == 6:
    mensaje = 'seis'
  elif numero == 7:
    mensaje = 'siete'
  elif numero == 8:
    mensaje = 'ocho'
  elif numero == 9:
    mensaje = 'nueve'
  else:
    mensaje = 'diez'

  return mensaje


print(numero_a_palabras(10))
