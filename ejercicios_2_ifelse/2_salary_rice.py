"""
En Naciones Unidas, para determinar el sueldo de un empleado, se clasifican los puestos con una letra y un
número (G1, G2, P1,P2,P3, P4, P5, P6, D1, D2). Las letras se corresponden a "General", "Profesional" y
"Directivo".
Se van a actualizar los sueldos de los de nivel P. Se te encarga que escribas una función salary_rise
que devuelva el porcentaje que le corresponde a cada uno de los P, siguendo los datos de abajo:
P1: 20%
P2: 22%
P3: 21%
P4: 19%
P5: 24%
P6: 15%
la función recibe el número (sin la p) y devuelve el porcentaje que corresponde.
¿Es una función total o parcial?
R: R: Total, ya que maneja todos los casos de entrada.
"""

def salary_rise(number):
  if number == 1:
    percentage = '20%'
  elif number == 2:
    percentage = "22%"
  elif number == 3:
    percentage = "21%"
  elif number == 4:
    percentage = "19%"
  elif number == 5:
    percentage= "24%"
  elif number == 6:
    percentage = "15%"
  else:
    percentage = "The data is out of range."
  return percentage

print(salary_rise(4))
print(salary_rise(44))
print(salary_rise(6))
print(salary_rise(-6))