"""
Crea la función is_sum_seq . Recibe una lista de números y devuelve True si cada elemento es
la suma de todos los anteriores.
1. La lista tienen que tener al menos 3 elementos (para que el tercero sea la suma de los
anteriores). En caso contrario, debe de devolver False
2. La función no debe de recorrer más elementos de la lista de los necesarios.
3. El primer elemento que se debe de inspeccionar es el tercero.
"""

def is_sum_seq(numbers):
  is_sum_seq = False
  accum = 0
  if len(numbers) < 3:
      is_sum_seq = False
  for i in numbers:
    accum += i
    if accum == numbers[-1]:
      is_sum_seq = True
  return is_sum_seq

print(is_sum_seq([1,2,3,6,12,24]))
