"""
Crea la función double_if_neg que recibe una lista de números y devuelve una nueva lista de números con el siguiente cambio: si un número es negativo, se le multiplica por dos.
"""

def double_if_neg(numbers):
  new_list = []
  for number in numbers:
    if number < 0:
      number = number * 2
    new_list.append(number)
  return new_list

print(double_if_neg([1,2,-3,4,-5]))