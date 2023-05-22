"""
#14
Crea la función explode . Recibe una cadena y la convierte en una lista de caracteres.
Por ejemplo:
"hola" --> ["h", "o", "l", "a"] "" --> []
No vamos a trabajar sobre listas, sino sobre cadenas. No pasa nada, las cadenas son secuencias y se pueden manejar igual. Lo único que cambia es:
Vas a iterar por los caracteres de la cadena
¿Cual es el valor inicial del acumulador que vas a usar?
1. La función explode es reversible?
2. ¿Te acuerdas de implode ?
3. ¿Qué pasa si evalúas implode(explode("hola")) ?
"""
def explode(cadena):
  caracter_list = []
  for item in cadena:
    caracter_list.append(item)
  return caracter_list

print(explode('Hola'))
print(explode(''))