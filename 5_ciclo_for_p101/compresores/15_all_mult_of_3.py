"""
Crea la función all_mult_of_3 . Recibe una lista de números y devuelve True si todos son
múltiplos de 3.
1. ¿Qué tipo de función es all_equal
2. ¿Qué debería de devolver cuando recibe la lista vacía?
3. ¿Es una función total o parcial?
4. Asegúrate que tu función no recorre elementos innecesarios de la lista

"""

def all_mul_of_3(numbers_list):
  is_mul_of_3 = True
  for i in numbers_list:
    if i % 3 != 0:
      is_mul_of_3 = False
      break
  return is_mul_of_3

print(all_mul_of_3([3, 6, 9, 12, 15]))
print(all_mul_of_3([3, 2, 7, 5, 17]))
