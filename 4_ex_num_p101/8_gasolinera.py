"""
En una gasolinera tienen surtidores que dispensan la gasolina en galones, pero el precio está en litros.
Sabiendo que un galón son 3.784 litros, construye una función que con los galones repostados y el precio por litro como datos obtenga el precio a pagar.
"""

def price_to_pay(gallones, price):
  if gallones <= 0 or price <= 0:
    price = -1
  elif gallones > 0 and price > 0:
    price = round(gallones_liters(gallones) * price)
  return price

# función que calcula de galones a litros
def gallones_liters(gallones):
  LITER = gallones * 3.784
  return LITER

print(price_to_pay(10, 2.34))
print(price_to_pay(0, 0))
print(price_to_pay(-1, -2))
print(price_to_pay(10, -2))