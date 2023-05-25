"""
Crea la función rev que recibe una secuencia (lista o cadena) y la devuelve invertida.
rev([1,2,3,4]) == [4,3,2,1] rev("Hola") == "aloH"
Pista: Se trata de un transformador y puedes usar range con el tercer parámetro para iterar por los índices hacia atrás.
"""

def rev(secuencia):
  new_list = []
  if type(secuencia) == str:
    new_list = (secuencia[::-1])
  else:
    for i in range(len(secuencia) - 1, -1, -1):
      new_list.append(secuencia[i])
  return new_list

print(rev([1,2,3,4]))
print(rev('Hola'))
print(rev(['Hola', 'Pepe']))


