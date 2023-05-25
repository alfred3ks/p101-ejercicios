"""
Crea la función concat_vowels que recibe una lista de cadenas y devuelve la concatenación de todas aquellas cadenas que empiezan por una vocal.
Pist: DIVIDE & VENCERÁS. Resuelve primero el problema del predicado que indica si una cadena empieza por una vocal.
"""

def start_vowel(string):
  vowels_list = ['a','e','i','o','u']
  first_chart = False
  if string[0].lower() in vowels_list:
    first_chart = True
  return first_chart

def concat_vowels(list_elements):
  vowel_list = []
  index = 0
  while index < len(list_elements):
    if start_vowel(list_elements[index]):
      vowel_list.append(list_elements[index])
    index = index + 1
  return vowel_list

print(concat_vowels(['Avion', 'Elefante', 'Madrid']))