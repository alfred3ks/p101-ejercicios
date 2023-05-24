"""
Crea la función less_than(numbers, n) que recibe una lista de números y un número n.
Devuelve la lista de aquellos números que son menores o iguales a n.
1. ¿Qué tipo de función es (compresor, selector o transformador)?
2. ¿Qué debería de devolver cuando recibe una lista vacía?
3. Si te ayuda, impleméntala primero con for e identifica claramente los 4 elementos de la iteración.
"""
def lees_than(numbers, n):
  result = []
  index = 0
  while index < len(numbers):
    if numbers[index] <= n:
      result.append(numbers[index])
    index = index + 1
  return result

print(lees_than([1,2,3,4,5,6], 7))
