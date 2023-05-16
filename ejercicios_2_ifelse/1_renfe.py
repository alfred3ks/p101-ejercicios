"""
En Renfe te encargan una función para determinar el precios de los billetes con la siguiente promoción:
El billete de ida y vuelta a cualquier ciudad de España cuesta €0.1 por Km recorrido en el primer tramo.
Si la distancia es superior a 600 Km, el precio por Km baja a €0.08.
Si la distancia es inferior a 100 km, el coste por km es de €0.17
Si la vuelta es 7 días o más después de la ida, el precio total tiene un descuento del 12%.
Crea la función ticket_cost que recibe: distancia en km al destino final y número de dias entre la ida y la vuelta. Debe de devolver el coste total.
Pregunta:
¿Es una función total o parcial?
R: Parcial ya que no maneja todos los casos de entrada.
"""

def ticket_cost(distance, days):
  if distance < 0:
    cost_distance = -1
  elif distance > 600:
    cost_distance = distance * 0.08
  elif distance < 100:
    cost_distance = distance * 0.17
  else:
     cost_distance = distance * 0.1
  total_cost = cost_distance

  if days >= 7:
   total_cost = total_cost * 0.88
  return total_cost

print(ticket_cost(-400, 3))
print(ticket_cost(400, 3))
print(ticket_cost(601, 9))

