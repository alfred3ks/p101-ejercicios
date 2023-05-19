# Ejercicio 7
# 1. Crea la función euro_to_pta que recibe un número de euros y te devuelve la cantidad de Pesetas


def euro_to_pta(euros):
  """
  Calcula de euros a pesetas
  """
  pta = euros * 166
  return pta

print(euro_to_pta(0.001))


# 2. Ahora crea la función pta_to_euro que hace lo opuesto.
#A. ¿Podrías implementar pta_to_euro llamando a euro_to_pta (para reaprovechar código)?
def pta_to_euro(pta):
  """
  Calcula de pta a euros
  """
  # euros = pta / 166, al pasarle a la funcion euro_to_pta(1/pta) en la funcion saca 0.166 de retorno
  euros = 1 / euro_to_pta(1/pta)
  return euros

print(pta_to_euro(1000))