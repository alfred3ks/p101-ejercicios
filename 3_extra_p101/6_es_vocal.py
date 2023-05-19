"""
Crea la función es_vocal(letra) que acepta un carácter y devuelve True si es una vocal (mayúscula o minúscula) y False si no lo es.
Un carácter es una cadena que sólo tiene una letra. Por ejemplo "u" es un carácter, pero "uau" no lo es.
"""

def es_vocal(letra):
  if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
      mensage = True
  elif letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    mensage = True
  else:
    mensage = False
  return mensage;


print(es_vocal('AG'))


# Tenemos un ejemplo usando listas e iterando la lista
def is_vocal(letra):
  vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  if len(letra) != 1:
    mensage = False
  if letra in vocales:
    mensage = True
  else:
    mensage = False
  return mensage

print(is_vocal('e'))