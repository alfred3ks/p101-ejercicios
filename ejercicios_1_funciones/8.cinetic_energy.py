# Crea la función cinetic_energy(mass, speed) que acepta la masa y la velocidad de un objeto y
# devuelve la energía cinética del objeto, calculada con la fórmula: E = (1/2)mv².

def cinetic_energy(mass, speed):
  """
  Calcula la energia cinetica
  """
  e = (1/2)*mass* speed**2
  return e

print(cinetic_energy(10,23))