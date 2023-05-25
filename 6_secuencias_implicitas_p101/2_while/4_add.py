"""
Crea la función add(numbers, n) que recibe una lista de números y devuelve una nueva lista con los elementos originales + n.
Por ejemplo:
add([1,2,3,4,5], 2) --> [3,4,5,6,7]
"""

def add(numbers, num):
  list_numbers = []
  index = 0

  while index < len(numbers):
    list_numbers.append(numbers[index] * num)
    index = index + 1
  return list_numbers

print(add([1,2,3,4,5,6], 7))