"""
# Ejercicio 5:
Parte 1. Crea una función precio_final que calcule el precio final de un artículo en función de tres parámetros, el precio_base, el descuento a aplicar y el IVA.
El precio_base es un número flotante, el descuento es un porcentaje (elige tú si usarlo como tanto por uno (0.2) o como tanto por cien (20) y el IVA es, de nuevo un porcentaje a elegir entre (0, 4, 10 y 21) o (0, 0.04, 0.1 y 0.21).
Parte 2. Crea ahora una función para cada tipo de iva de manera que tengas precio_iva0 , precio_iva4 , precio_iva10 y precio_iva21 . Para todas ellas los parámetros serán el precio_base y el descuento a aplicar. Es decir, si aplicas precio_iva4 al precio_base 100 y descuento 0, el resultado será 104, si aplicas precio_iva4 al precio_base 100 y descuento 5, el resultado será 98,8
De igual manera, si los descuentos fueran 5, 10 y 15, puedes crear las funciones precio_dto5, precio_dto10 y precio_dto15 . En este caso sus parámetros de entrada serán precio_base e IVA.
"""
# parte 1:
def final_price(base_price, discount, tax):
  precio_descuento = base_price * ((100 - discount) / 100)
  if tax == 0:
    final_price = precio_descuento * ((100 + tax) / 100)
  elif tax == 4:
    final_price = precio_descuento * ((100 + tax) / 100)
  elif tax == 10:
    final_price = precio_descuento * ((100 + tax) / 100)
  elif tax == 21:
    final_price = precio_descuento * ((100 + tax) / 100)
  else:
    final_price = -1
  return final_price

print(final_price(200, 15, 0))
print(final_price(100, 20, 4))
print(final_price(100, 20, 10))
print(final_price(100, 20, 21))
print(final_price(100, 20, 22))

# parte 2:
# Definimos una funcion para cada tipo de iva:
def tax_price_0(base_price, discount):
  tax = 0
  tax_price = round(final_price(base_price, discount, tax),2)
  return tax_price

def tax_price_4(base_price, discount):
  tax = 4
  tax_price = round(final_price(base_price, discount, tax),2)
  return tax_price

def tax_price_10(base_price, discount):
  tax = 10
  tax_price = round(final_price(base_price, discount, tax),2)
  return tax_price

def tax_price_21(base_price, discount):
  tax = 21
  tax_price = round(final_price(base_price, discount, tax),2)
  return tax_price

print(tax_price_0(200, 15))
print(tax_price_4(200, 15))
print(tax_price_10(200, 15))
print(tax_price_21(200, 15))
