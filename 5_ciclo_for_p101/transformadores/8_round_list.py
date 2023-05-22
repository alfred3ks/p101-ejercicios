"""
#8:
Necesitas una función que recibe una lista de números y los redondea a varias posiciones decimales (1, 2,4, etc).
Modifica round_list para que pueda hacer eso.
Aqui vemos cuando pasamos un valor por defecto, parametros por defecto, por si no nos envia el valor.
"""

def round_list_new(elements, position = 2):
  new_list = []
  for element in elements:
    number = round(float(element), position)
    new_list.append(number)
  return new_list

print(round_list_new([1.016, 8.023, 42.009], 3))
print(round_list_new([1.016, 8.023, 42.009]))