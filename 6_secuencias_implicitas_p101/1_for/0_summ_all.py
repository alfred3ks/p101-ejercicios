"""
Crea una función sum_all que recibe 3 parámetros:
Un valor de inicio
Un valor final
Un valor de paso
y devuelve la suma de todos los valores de inicio a fin tomados de paso en paso.
Es decir,
sum_all(1, 10, 2) sumaría 1,3,5,7 y 9.
Recuerda usar range
"""

# ejercicios 0 de clase de for con range for implicito: Un compresor.
def sum_all(start, end, step):
  """
  Devuelve la suma de todos los numeros de start hasta end - 1 de step en step
  """
  accum = 0
  for number in range(start, end, step):
    accum = accum + number
  return accum

print(sum_all(1,10,2))
print(sum_all(1,100,22))


print(dir(sum_all))
print(sum_all.__doc__)
print(range.__doc__)

# Aqui vemos todas las opciones de range()
def imprimeX():
  list_number = []
  for x in range(30):
    list_number.append(x)
  return list_number

def imprimeY():
  list_number = []
  for x in range(2,30):
    list_number.append(x)
  return list_number

def imprimeZ():
  list_number = []
  for x in range(2,30,3):
    list_number.append(x)
  return list_number

print(imprimeX())
print(imprimeY())
print(imprimeZ())
