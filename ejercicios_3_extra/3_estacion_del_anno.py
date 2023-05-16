"""
Crea la función estacion_del_anno(mes) que acepta un mes (1-12) y devuelve una cadena que indica la
estación del año correspondiente en el hemisferio norte: primavera, verano, otoño o invierno.
"""

def estacion_del_anno(mes):
  # Validar el rango del mes
  if mes < 1 or mes > 12:
    mensaje = "Mes inválido. El mes debe estar en el rango de 1 a 12."

  # Determinar la estación del año
  elif mes >= 3 and mes <= 5:
    mensaje = "Primavera"
  elif mes >= 6 and mes <= 8:
    mensaje = "Verano"
  elif mes >= 9 and mes <= 11:
    mensaje = "Otoño"
  else:
    mensaje = "Invierno"
  return mensaje

print(estacion_del_anno(4))
print(estacion_del_anno(1))
print(estacion_del_anno(10))
print(estacion_del_anno(12))
print(estacion_del_anno(220))