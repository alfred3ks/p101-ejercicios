"""
#1
Crea la función select_even que recibe una lista de números y devuelve una lista con sólo los números
pares, en el mismo orden.
Es decir, si recibe la lista [1,2,3,4,5,6] , el valor correcto de retorno es [2,4,6] . No es correcto
devolver [4, 2, 6] .
¿Qué debe de devolver si no hay ningún numero par?
¿Qué debe de devolver si recibe la lista vacía?
"""
def select_even(elements):
  numbers = []
  for element in elements:
    if element % 2 == 0:
      numbers.append(element)
  return numbers

# print(select_even([1,2,3,4,5,6]))
# print(select_even([1,3,5,]))
# print(select_even([]))