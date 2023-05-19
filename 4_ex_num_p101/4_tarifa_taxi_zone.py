"""
# Ejercicio 4:
Sabiendo que la tarifa de taxi de una ciudad es 2,5 € por el inicio del servicio mas 46 centimos de euro por cada 400 metros de recorrido en la zona 1 y 69 centimos de euro por cada 400 metros de recorrido en la zona 2.
Parte 1. Crea una función que devuelva el precio de una carrera indicando los kilómetros (no los metros) recorridos y la zona (por simplificar supondremos que todas las carreras son sin cambiar de zona).
Si se informa una distancia recorrida menor que cero o una zona desconocida la función debe devolver el valor -1 (indicativo de error)
Parte 2. Utilizando la función anterior crear otras dos funciones una llamada carreraZ1 y otra llamada carreraZ2 cuyo único parámetro de entrada sea los kilómetros recorridos y que devuelvan respectivamente el precio de la carrera en la zona 1 y en la zona 2.
"""
def taxi_fare_zone(distance, zone):
  price = 0
  min_fare = 2.5
  zone1_per_400_meter = 0.46
  zone2_per_400_meter = 0.69
  # Aqui calculamos la distancia en metros y hacemos la equivalencia a 400 mtrs:
  dist400 = distance * 1000 / 400

  # valido que la distancia no sea negativa y las zonas
  if distance < 0 or (zone != 1 and zone != 2):
    # es un error!!!
    price = -1
  elif zone == 1:
    price = dist400 * zone1_per_400_meter
    price = price + min_fare
  elif zone == 2:
    price = dist400 * zone2_per_400_meter
    price = price + min_fare
  return price

print(taxi_fare_zone(-100, 1))
print(taxi_fare_zone(100, 3))
print(taxi_fare_zone(100, 1))
print(taxi_fare_zone(100, 2))

#parte 2
def carreraz1(distance):
  return taxi_fare_zone(distance, 1)
print(carreraz1(120))

def carreraz2(distance):
  return taxi_fare_zone(distance, 2)
print(carreraz2(120))
