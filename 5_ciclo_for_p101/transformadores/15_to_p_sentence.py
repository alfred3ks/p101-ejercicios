"""
La Lengua de la P es un juego de niños común en Brasil en el que se alteran las palabras convirtiéndolas en una especie de trabalenguas.
Si una letra es una vocal, se le transforma en una sílaba con la p y las dos vocales:
a -> apa
e -> epe
i -> ipi
o -> opo
u -> upu
Aplicando esto, las siguientes palabras se convertirían así:
Basico -> Bapasipicopo
Raro -> Raparopo
Alamo -> Apalapamopo
Crea la función to_p_sentence que recibe una frase (una cadena) y la convierte a la Lengua de la P.
PISTAS
1. DIVIDE & VENCERÁS: lo más sencillo sería convertir un caracter a la lengua de la p. Para ello, si es una vocal, aplicas las normas de arriba, y si es cualquier otra cosa, se deja tal cual.
2. Cuando tengas eso resuelto, intenta aplicarlo a una frase.
"""

def to_p_char(char):
  vowels = ['a', 'e', 'i', 'o', 'u']
  new_list_char = []
  phrase = ''
  if char in vowels:
    phrase = char + 'p' + char
    new_list_char.append(phrase)
  else:
    new_list_char.append(char)
  return new_list_char

print(to_p_char('a'))
print(to_p_char('e'))
print(to_p_char('i'))
print(to_p_char('o'))
print(to_p_char('u'))
print(to_p_char('x'))

def to_p_sentence(phrase):
  for letter in phrase:
    pass
