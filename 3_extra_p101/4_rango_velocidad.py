"""
Crea la función rango_velocidad(velocidad) que acepta una velocidad en km/h y devuelve una cadena que
indica si la velocidad es "Lenta", "Moderada", "Rápida" o "Muy rápida".
"""

def rango_velocidad(velocidad):
  if velocidad < 0:
    mensaje = 'La velocidad no puede ser negativa'
  elif velocidad <= 60:
    mensaje = 'Tu velocidad es lenta'
  elif velocidad <= 80:
    mensaje = 'Tu velocidad es moderada'
  elif velocidad <=100:
    mensaje = 'Tu velocidad es rápida'
  else:
    mensaje = 'Tu velocidad es muy rápida'
  return mensaje;

print(rango_velocidad(-1))
print(rango_velocidad(35))
print(rango_velocidad(71))
print(rango_velocidad(85))
print(rango_velocidad(125))
