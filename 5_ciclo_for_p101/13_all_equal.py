"""
Crea la función all_equal . Recibe una lista (de lo que sea) y devuelve True si todos los elementos son iguales entre sí y False en caso contrario.
Por ejemplo:
all_equal([1,1,1]) -> True all_equal(["hola", "Mundo"]) -> False
1. ¿Qué tipo de función es all_equal
2. ¿Qué debería de devolver cuando recibe la lista vacía?
3. ¿Es una función total o parcial?
4. Asegúrate que tu función no recorre elementos innecesarios de la lista
NOTA: La lista vacia: [] devuelve debe devolver True
"""

data = [1,1,1]
# data = ['Hola', 'Mundo']
data = ['Hola', 'Hola']
# data = []

def all_equal(data_list):
  # almacenamos el primer elemento de la lista para compararlo con el resto. Inicializamos a False
  result = True
  # Comprobamos que la lista no sea vacia:
  if data_list != []:
    first = data[0]
    for e in data_list:
      if first == e:
        result = True
      else:
        result = False
        break
  return result

print(all_equal(data))