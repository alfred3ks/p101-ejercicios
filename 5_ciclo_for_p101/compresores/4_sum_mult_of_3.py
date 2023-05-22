"""
Crea la función sum_mult_of_3 :
Recibe una lista de números
Devuelve la suma de aquellos que son múltiplos de 3
DIVIDE & VENCERÁS
Resuelve primero el subproblema "saber si un número es múltiplo de 3", creando el predicado
is_multiple_3 . Recuerda el operador % para obtener el resto de una división.
"""

numbers = [1,2,3,4,5,6,7,8,9]

def sum_mul_of_3(numbers):
  total = 0
  for number in numbers:
    if number % 3 == 0:
      total += number
  return total

print(sum_mul_of_3(numbers))