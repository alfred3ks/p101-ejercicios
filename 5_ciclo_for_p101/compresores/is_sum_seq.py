"""
Crea la función is_sum_seq . Recibe una lista de números y devuelve True si cada elemento es
la suma de todos los anteriores.
1. La lista tienen que tener al menos 3 elementos (para que el tercero sea la suma de los
anteriores). En caso contrario, debe de devolver False
2. La función no debe de recorrer más elementos de la lista de los necesarios.
3. El primer elemento que se debe de inspeccionar es el tercero.
"""

def is_sum_seq(numbers):
  is_sum_seq = True
  for i in numbers:
      is_sum_seq = False
      break
  return is_sum_seq

print(is_sum_seq([3,5,8]))
# print(is_sum_seq([1,2,3,5,8,13]))
