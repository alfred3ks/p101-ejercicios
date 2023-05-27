"""
Crea la función select_long_words . Recibe dos parámetros:
1. Un número
2. Una lista de cadenas
Devuelve la lista de las palabras cuya longitud sea igual o mayor que el número.
¿Qué devolverías si el número es negativo o cero?
¿Qué devolverías si recibes una lista vacía?
"""

def count_word(word):
  count_word = len(word)
  return count_word

def select_log_words(num, list_string):
  new_list = []
  for item in list_string:
    if num > 0 and list_string != []:
      if count_word(item)  >= num:
        new_list.append(item)
  return new_list

print(select_log_words(3,['hola', 'mundo','en','python','con', 'Keepcoding']))
print(select_log_words(-1,['hola', 'mundo','en','python','con', 'Keepcoding']))
print(select_log_words(4,[]))
