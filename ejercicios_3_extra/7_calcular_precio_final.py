"""
Crea la función calcular_precio_final(precio, impuesto, descuento) que acepta el precio original de un producto, el porcentaje de impuesto y el porcentaje de descuento, y devuelve el precio final después de aplicar el impuesto y el descuento.
"""

def calcular_precio_final(precio, impuesto, descuento):
  if impuesto == 21:
    precio_con_descuento = precio * (1 - ( descuento / 100 ))
    precio_final = precio_con_descuento * (1 + ( impuesto / 100 ))
  else:
    precio_final = -1
  return precio_final

print(calcular_precio_final(200, 21,0))