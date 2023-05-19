"""
Crea la función tipo_triangulo(a, b, c) que acepta las longitudes de los tres lados de un triángulo y devuelve
una cadena que indica si el triángulo es equilátero, isósceles o escaleno.
"""

def tipo_triangulo(a, b, c):
  if a <= 0 or b <= 0 or c <= 0:
    return "Los lados deben tener longitudes positivas."
  elif a == b and a == c and b == c:
    result = 'Equilátero'
  elif a != b and a != c and b != c:
    result = 'Escaleno'
  elif a == b and a != c and b != c:
    result = 'Isósceles'
  return result

print(tipo_triangulo(22,22,22))
print(tipo_triangulo(24,22,34))
print(tipo_triangulo(22,22,34))
print(tipo_triangulo(0,22,34))