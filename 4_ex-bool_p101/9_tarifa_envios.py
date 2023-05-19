"""
Supongamos que estás construyendo un programa para una empresa de envío de paquetes que debe calcular la tarifa de envío para cada paquete. El costo de envío depende del peso del paquete, la distancia recorrida y el tipo de envío (por ejemplo, estándar o express). Además, hay descuentos disponibles para paquetes grandes o para clientes habituales.
Para calcular la tarifa de envío, primero deberás pedir al usuario que proporcione la siguiente información:
- Peso del paquete en kilogramos
- Distancia recorrida en kilómetros
- Tipo de envío (estándar o express)
- Si el paquete es grande (sí o no)
- Si el cliente es habitual (sí o no)
A continuación, deberás calcular la tarifa de envío utilizando la siguiente fórmula:
- Si el peso del paquete es menor o igual a 10 kg, la tarifa es de 5€ por kilómetro recorrido para el envío estándar o 8€ por kilómetro recorrido para el envío express.
- Si el peso del paquete es mayor que 10 kg pero menor o igual a 25 kg, la tarifa es de 7€ por kilómetro recorrido para el envío estándar o 12€ por kilómetro recorrido para el envío express.
- Si el peso del paquete es mayor que 25 kg, la tarifa es de 10€ por kilómetro recorrido para el envío estándar o 15€ por kilómetro recorrido para el envío express.
- Si el paquete es grande, se aplicará un descuento del 10% sobre el costo total del envío. Si el cliente es habitual, se aplicará un descuento adicional del 5% sobre el costo total del envío.
- Construye una función que usando esos datos, devuelva el precio por kilómetro a aplicar y otra que indique el precio final con los descuentos aplicados.
"""

def cost_per_envio(weight, distance, shipping_type, isBig, isClient):
  pass