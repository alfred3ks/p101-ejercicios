# Codigo realizado en clase:

from enum import Enum

class PackageType (Enum):
  STANDARD = 0
  EXPRESS = 1
  INSURED = 2

def cost_of_sending(weight, distance, package_type, is_big, is_premium_client):
  descuento_grande = 0
  descuento_habitual = 0
  tarifa = 0

  if package_type == PackageType.STANDARD:
    if weight <= 10:
      tarifa = 5
    elif weight <= 25:
      tarifa = 7
    else:
      tarifa = 10
  elif package_type == PackageType.EXPRESS:
    if weight <= 10:
      tarifa = 8
    elif weight <= 25:
      tarifa = 12
    else:
      tarifa = 15
  else:
    # Es un paquete asegurado:
    tarifa = 50

  if is_big == True:
    descuento_grande = 10/100

  if is_premium_client == True:
    descuento_habitual = 5/100

  final_total = distance * tarifa
  precio_descuento_tamanio = final_total * descuento_grande
  precio_descuento_cliente = final_total * descuento_habitual

  precio_total = final_total - precio_descuento_tamanio - precio_descuento_cliente

  return precio_total

print(cost_of_sending(weight = 10, distance = 100, package_type = PackageType.EXPRESS, is_big = True, is_premium_client = False))