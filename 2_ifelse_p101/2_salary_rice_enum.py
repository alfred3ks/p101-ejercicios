"""
En Naciones Unidas, para determinar el sueldo de un empleado, se clasifican los puestos con una letra y un número (G1, G2, P1,P2,P3, P4, P5, P6, D1, D2). Las letras se corresponden a "General", "Profesional" y "Directivo".
Se van a actualizar los sueldos de los empleados. Se te encarga que escribas una función salary_rise que devuelva el nuevo sueldo que le corresponde a cada uno, siguendo los datos de abajo:

  P1: 20%
  P2: 22%
  P3: 21%
  P4: 19%
  P5: 24%
  P6: 15%
  G1: 0%
  G2: 0%
  D1: 60%
  D2: 300%

la función recibe el tipo de empleado mediante una enum que tiene todos los casos y el sueldo actual. Devuelve el sueldo actualizado.
¿Es una función total o parcial?
"""
from enum import Enum

class EmployeeType (Enum):
  P1 = 0
  P2 = 1
  P3 = 2
  P4 = 3
  P5 = 4
  P6 = 5
  G1 = 6
  G2 = 7
  D1 = 8
  D2 = 9

def salary_rise(type_employee, current_salary):
  update_salary = 0

  if type_employee == EmployeeType.G1 and type_employee == EmployeeType.G2:
    update_salary = current_salary
  elif type_employee == EmployeeType.P6:
    update_salary = current_salary * 1.15
  elif type_employee == EmployeeType.P4:
    update_salary = current_salary * 1.19
  elif type_employee == EmployeeType.P1:
    update_salary = current_salary * 1.2
  elif type_employee == EmployeeType.P3:
    update_salary = current_salary * 1.21
  elif type_employee == EmployeeType.P5:
    update_salary = current_salary * 1.24
  elif type_employee == EmployeeType.D1:
    update_salary = current_salary * 1.6
  elif type_employee == EmployeeType.D2:
    update_salary = current_salary * 3
  else:
    update_salary = -1
  return update_salary

print(salary_rise('P1', -1))
print(salary_rise(EmployeeType.P3, 1000))
print(salary_rise(EmployeeType.D2, 2000))

