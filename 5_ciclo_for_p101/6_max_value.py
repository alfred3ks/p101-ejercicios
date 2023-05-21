"""
Crea la función max_value que recibe una lista y devuelve el mayor elemento de la misma.

¿Qué crees que debe de hacer si todos son iguales?
¿Qué crees que debe de devolver en caso de recibir la lista vacía?

Es siempre una buena idea que las funciones sean totales. A veces lo podemos lograr ampliando el valor de retorno. De esta manera, conseguimos eliminar los casos especiales (como que la lista de entrada es la lista vacía). Esto hace que el uso de la función sea más sencillo y se reducen las posibilidades de errores.

Cerveza para todos. Elimina los casos especiales

¿Cual es el valor máximo de una lista, cuando la lista está vacía? En Español, diríamos ninguno. En
Python, se dice None .
None es la única instancia del typo NoneType y se usa para indicar la nada.
Entre los tipos de Python, juego el mismo papel que el 0 entre los números.
1. Refactoriza tu función max_value para que en el caso de que la lista de entrada sea la vacía, que
devuelva None .
2. Crea la función min_value que devuelve el valor mínimo.
3. Compara ambas. ¿Qué partes son comunes y qué partes son distintas?
"""

numbers = [10,22,37,84,15,76,47,88,999,67]
numbers = [-5, -7, -2]
numbers = []

def max_value(numbers):
  result = None
  if len(numbers) > 0:
    max = numbers[0]
  else:
    max = result
  for number in numbers:
    if number > max:
      max = number
  return max

print(max_value(numbers))

# Opcion B:

def max_value_a(numbers):
  result = None
  if numbers != []:
    max = numbers[0]
    for number in numbers:
      if number > max:
        max = number
    result = max
  return result

print(max_value_a(numbers))