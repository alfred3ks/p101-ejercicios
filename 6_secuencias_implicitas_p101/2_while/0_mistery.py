"""
1. ¿Qué hace la siguiente función?
2. Rellena la información que falta para que funcione
3. Identifica los 4 componentes de la iteración
"""

"""
def mistery(elements):
sum = 0
i = 0
  while i < len(???):
    sum = sum + elements[???]
    i = i + 1
return ???
"""

def mistery(elements):
  sum = 0
  i = 0
  while i < len(elements):
    sum = sum + elements[i]
    i = i + 1
  return sum

# Aqui tenemos la funcion que pone en ejemplo en clase:
def find_event_number(numbers):
  found = False
  index = 0
  while not found or index < len(numbers):
    if numbers[index] % 2 == 0:
      found = True
    index = index + 1
  return found

print(find_event_number([1,3,4,5,6]))

