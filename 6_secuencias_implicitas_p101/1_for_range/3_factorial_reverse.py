"""
Ahora calcúlalo al revés, yendo de n hasta 1. Recuerda el tercer parámetro de la función range
"""

def factorial(n):
  accum = 1
  m = abs(n)
  for num in range(m, accum, -1):
    accum = accum * num
  return accum

print(factorial(4))
print(factorial(3))
print(factorial(1))
print(factorial(0))
print(factorial(-5))