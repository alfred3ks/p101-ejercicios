"""
Crea la función select_starts . Recibe dos parámetros:
1. Una cadena
2. Una lista de cadenas
Devuelve una lista con aquellas cadenas que empiezan por la cadena que has recibido como
parámetro.
¿Qué devolverías cunado recibes una lista vacía?
¿ select_starts es total o parcial?
"""

def select_starts(string, elements):
  new_list = []
  for element in elements:
    if string in element:
      new_list.append(element)
  return new_list

print(select_starts('pibe',['pibe_de_oro','pibe', 'orca', 'pibeincircus']))