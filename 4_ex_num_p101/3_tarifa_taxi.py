"""
# Ejercicio 3:
Sabiendo que la tarifa de taxi de una ciudad es 2,5 € por el inicio del servicio mas 46 centimos de euro por cada 400 metros de recorrido. Crea una función que devuelva el precio de una carrera indicando los kilómetros (no los metros) recorridos.
Si se informa una distancia recorrida menor que cero, la función debe devolver el valor -1 (indicativo de error)

"""
def taxi_fare(distance):
  """
  Recibe distancia en KM y devuelve el coste en euros, si la distancia es cero devuelve el inicio de tarifa, si la distancia es negativa lo cual es un error devuelve -1 para indicarlo
  """
  # declaro las variables
  price = 0
  min_fare = 2.5
  cost_per_400_meter = 0.46

  # valido que la distancia no sea negativa
  if distance < 0:
    # es un error!!!
    price = -1
  else:
    # convierto la distancia de entrada a metros
    dist = distance * 1000
    # lo convierto en tramos de 400 m y multiplico por el coste, le sumo los 2.5
    dist = dist / 400
    # calculo el precio
    price = dist * cost_per_400_meter
    price = price + min_fare

  return price

print(taxi_fare(-100))
print(taxi_fare(0))
print(taxi_fare(1))
