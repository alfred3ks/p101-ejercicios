"""
Crea la función tiempo_a_segundos(horas, minutos, segundos) que acepta horas, minutos y segundos y devuelve el tiempo total en segundos
"""

def tiempo_a_segundos(horas, minutos, segundos):
  una_hora = 60
  un_minuto = 60
  tiempo_segundos = (horas * una_hora * un_minuto) + (minutos * un_minuto) + segundos
  return tiempo_segundos

print(tiempo_a_segundos(1,0,0))
print(tiempo_a_segundos(5,34,10))