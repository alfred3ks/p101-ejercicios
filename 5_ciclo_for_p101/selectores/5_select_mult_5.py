"""
Crea la función select_mult_5 . Recibe una lista de números y devuelve una lista con aquellos que son múltiplos de 5.
"""

def select_mult_5(numbers):
  new_list = []
  for number in numbers:
    if number % 5 == 0:
      new_list.append(number)
  return new_list

print(select_mult_5([1,23,5,15,78,3,25]))