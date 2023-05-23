"""
#7
Crea la función select_starts_letter . Recibe dos parámetros:
1. Una cadena de longitud 1 (un caracter)
2. Una lista de cadenas
Devuelve la lista de aquellas cadenas que empiezan por el carcter que has recibido. Respeta el orden.
La primera cadena ha de ser un sólo caracter. Si no es así, la función no debería de continuar.
Una forma de comprobar que un parámetro cumple una cierta condición es con la palabra clave assert

Assert en Python
El uso de assert en Python nos permite realizar comprobaciones. Si la expresión contenida dentro del mismo es False, se lanzará una excepción, concretamente AssertionError.
"""
# Opcion 1:
def select_start_letter(cadena, elements):
  new_list = []
  un_solo_caracter = cadena[0]
  if len(un_solo_caracter) != 1:
    assert False
  else:
    for element in elements:
      if element[0] == un_solo_caracter:
        new_list.append(element)
  return new_list

# Opcion 2: Profesor, mas condensado y mas simple:
def select_start_letter(caracter, elements):
  # Si esto se cumple sigue el resto sino se sale:
  # Ver documentacion de python assert:
  assert len(caracter) == 1

  new_list = []
  for element in elements:
    if element[0] == caracter:
      new_list.append(element)
  return new_list

# print(select_start_letter('asd', ['a','dddd']))
print(select_start_letter('a', ['a','dddd']))