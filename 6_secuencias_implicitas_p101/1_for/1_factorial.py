"""
Crea la función factorial(n) que recibe un número y devuelve su factorial.
Recuerda que el factorial (representado con un !) de un número n es la multiplicación de todos los números enteros de 1 hasta n:

  4! = 4 * 3 * 2 * 1

sabiendo que: 1! = 1 0! = 1

Hazlo usando range yendo de 1 hasta n.

Nota:
range(a,b) donde b = b -1
Por eso tenemos que poner m +1 porque el factorial debe ir:
n! = n(n-1)
"""

def factorial(n):
  accum = 1
  for num in range(1, n + 1):
    accum = accum * num
  return accum

# print(factorial(4))
# print(factorial(3))
# print(factorial(1))
# print(factorial(0))
# print(factorial(-5))

"""
range(1, m + 1):
En este caso el rango va de 1 al n + 1, para el caso que n = 4 entonces el rango iria de 1 a 5:
valores iniciales:
accum = 1
num = 4

en la primera vuelta del for  num = 1 * accum = 1 -> 1
en la segunda vuelta vale     num = 2 * accum = 1 -> 2
en la tercera vuelta vale     num = 3 * accum = 2 -> 6
en la cuarta vuelta vale      num = 4 * accum = 6 -> 24

Y termina el ciclo y retorn 24
"""
