"""
#10
Crea la función update_salaries que recibe una lista de nóminas y crea una nueva lista con las nóminas aplicando los siguientes cambios:
nómina < 900 se incrementa en un 30%
900 <= nómina < 1500, se incrementa en un 12%
1500 <= nómina < 6000, se queda tal cual
nómina > 6000, se incrementa en un 100% (ventajas de ser alto cargo)
"""

def update_salaries(salaries_list):
    salaries_list_new = []
    for item in salaries_list:
        if item < 900:
            new_salari = item + (item * 0.30)
            salaries_list_new.append(new_salari)
        elif item >= 900 and item < 1500:
            new_salari = item + (item * 0.12)
            salaries_list_new.append(new_salari)
        elif item >= 1500 and item < 6000:
            new_salari = item + (item * 0)
            salaries_list_new.append(new_salari)
        elif item >6000:
            new_salari = item + (item * 1)
            salaries_list_new.append(new_salari)
    return salaries_list_new

print(update_salaries([888,1211,4900,7500]))

#Ejercicio (11)
def summ_all(num_list_salaries):
    total = 0
    for item in num_list_salaries:
        total = total + item

    return total

print(summ_all(update_salaries([888,1211,4900,7500])))