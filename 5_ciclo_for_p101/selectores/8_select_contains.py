"""
#8
Crea la función la función select_contains . Recibe dos parámetros:
1. Una cadena de cualquier longitud
2. Una lista de cadenas
Devuelve una lista de aquellas cadenas que contienen la recibida como parámetro, en cualquier posición
(principio, em medio, final, no importa)
DIVIDE & VENCERAS
Tienes un subproblema: averiguar si una cadena contiene a otra. Resuelve eso primero.
Teniendo en cuenta que la cadena A sólo puede ser una subcadena de la cadena B, si len(A) <=
len(B) , ¿cómo usarías tú eso para evitar que select_contains haga operaciones innecesarias?
"""

def select_containt(cadena, elements):
  contains = []
  for element in elements:
    if len(element) >= len(cadena) and cadena in element:
      contains.append(element)
  return contains

print(select_containt('huesos', ["hola", "mundo", "Quebrantahuesos"]))