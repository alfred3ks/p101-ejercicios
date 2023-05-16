"""
# Ejercicio 5:
Parte 1. Crea una función precio_final que calcule el precio final de un artículo en función de tres parámetros, el precio_base, el descuento a aplicar y el IVA.
El precio_base es un número flotante, el descuento es un porcentaje (elige tú si usarlo como tanto por uno (0.2) o como tanto por cien (20) y el IVA es, de nuevo un porcentaje a elegir entre (0, 4, 10 y 21) o (0, 0.04, 0.1 y 0.21).
Parte 2. Crea ahora una función para cada tipo de iva de manera que tengas precio_iva0 , precio_iva4 , precio_iva10 y precio_iva21 . Para todas ellas los parámetros serán el precio_base y el descuento a aplicar. Es decir, si aplicas precio_iva4 al precio_base 100 y descuento 0, el resultado será 104, si aplicas precio_iva4 al precio_base 100 y descuento 5, el resultado será 98,8
De igual manera, si los descuentos fueran 5, 10 y 15, puedes crear las funciones precio_dto5, precio_dto10 y precio_dto15 . En este caso sus parámetros de entrada serán precio_base e IVA.
"""

def precio_final(precio_base, descuento, iva):
  precio_descuento = precio_base * ((100 - descuento) / 100)
  if iva == 0:
    precio_final = precio_descuento * ((100 - iva) / 100)
  elif iva == 4:
    precio_final = precio_descuento * ((100 - iva) / 100)
  elif iva == 10:
    precio_final = precio_descuento * ((100 - iva) / 100)
  elif iva == 21:
    precio_final = precio_descuento * ((100 - iva) / 100)
  else:
    precio_final = -1
  return precio_final

print(precio_final(100, 20, 0))
print(precio_final(100, 20, 4))
print(precio_final(100, 20, 10))
print(precio_final(100, 20, 21))
print(precio_final(100, 20, 22))




