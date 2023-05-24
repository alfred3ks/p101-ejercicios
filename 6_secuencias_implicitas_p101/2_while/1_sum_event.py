"""
Crea la función sum_even que recibe una lista de números y devuelve la suma de los números
pares.
Recuerda los 4 elementos de la iteración.
"""

def sum_event(numbers):
  accum = 0
  index = 0
  while index < len(numbers):
    if numbers[index] % 2 == 0:
      accum = accum + numbers[index]
    index = index + 1
  return accum

print(sum_event([1,2,3]))
print(sum_event([2,4,6]))
print(sum_event([3,5,9]))
print(sum_event([]))
