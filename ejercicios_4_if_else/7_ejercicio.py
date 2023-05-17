"""
# Ejercicio 7:
Lo que te pedimos en este ejercicio es que pases esos colores a un nivel de porcentaje de negro
para transformar un color en gris.
Sin embargo el rojo, verde y azul no participan por igual en el gris. El rojo representa
aproximadamente el 30% del gris, el verde el 59% y el azul el 11%.
Se trata de construir una función que partiendo del color RGB como tres valores independientes
entre cero y 255 devuelva el valor de gris.
Trata de hacerlo con composición de funciones:
Primero trata de construir las funciones individuales que obtienen el nivel de gris de cada color y
la última la que obtiene el total de gris con los otros tres.
"""
# Opcion mia:
def color_red(red):
  red = red * 0.3
  return red

def color_green(green):
  green = green * 0.59
  return green

def color_blue(blue):
  blue = blue * 0.11
  return blue

def color_gray(red, green, blue):
  if red < 0 or red > 255:
    result = -1
  elif green < 0 or green > 255:
    result = -1
  elif blue < 0 or blue > 255:
    result = -1
  else:
    result = round(color_red(red) + color_green(green) + color_blue(blue))
  return result

# print(color_gray(12,255,56))
# print(color_gray(0,0,0))


"""
# Resolucion de la clase: Aqui lo que debe quedarnos es que hacemos la carta de los reyes, creamos nuestra funcion general y pasamos las funciones que vamos a necesitar luego las creamos.
"""
def rgb_to_gray(r, g, b):
  # Creo una variable para devolver el gris
  color_gray = 0
  # Compruebo que ninguno de los valores estan fuera de rango. Si esta devuelvo -1
  if not color_is_valid(r,g,b):
    color_gray = -1
  else:
  # Si todo esta bien calculo el valor del gris
    color_gray = round(r_to_gray(r,g,b) + g_to_gray(r,g,b) + b_to_gray(r,g,b))
  # Devuelvo el valor del gris
  return color_gray

# Creo la funcion para validar el color que este entre 0 y 255:
def color_is_valid(r,g,b):
  if r < 0 or r > 255:
    result = False
  elif g < 0 or g > 255:
    result = False
  elif b < 0 or b > 255:
    result = False
  else:
    result = True
  return result

# Creo las funciones que calculan los colores:
def r_to_gray(r,g,b):
  return r * 0.30

def g_to_gray(r,g,b):
  return g * 0.59

def b_to_gray(r,g,b):
  return b * 0.11

print(rgb_to_gray(0,0,0))
print(rgb_to_gray(255,255,255))
print(rgb_to_gray(56,255,255))
print(rgb_to_gray(-1,255,255))
print(rgb_to_gray(0,255,259))