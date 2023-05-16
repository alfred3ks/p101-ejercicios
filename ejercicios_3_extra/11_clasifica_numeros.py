"""
Crea la función clasifica_numeros(a, b, c) que acepta tres números enteros y devuelve una cadena que indica si los números están en orden ascendente, descendente o si no tienen un orden específico.
"""
def clasifica_numeros(a, b, c):
  if a < b < c:
    message = "Ascendente"
  elif a > b > c:
    message = "Descendente"
  else:
    message = "Sin orden específico"
  return message

print(clasifica_numeros(1,2,3))
print(clasifica_numeros(3,2,1))
print(clasifica_numeros(1,6,3))