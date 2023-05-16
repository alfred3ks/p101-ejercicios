"""
Tenemos estas dos funciones matemáticas y tienes que crear las funciones de Python equivalentes:

f(x,y) = (x**2 + y**2) / (x - y)

f(m,n) = (m**2 - n**2 + n) / m * n

1. Prueba ambas funciones con varios valores para asegurarte que funcionan bien.
2. ¿Hay algún valor de x o y que haga que haga que (a) estalle?
3. ¿Hay algún valor de m o n que haga que (b) estalle?
4. En la función cuadrática anterior, ¿hay algún valor de x que haga que la función estalle?

Las funciones (a) y (b) son parciales
Si x e y son iguales, a f(x,y) le dá un jamacuco
Si m o n son cero, a f(m,n) le dá un jamacuco
"""

def fun1(x,y):
  result = (x**2 + y**2) / (x - y)
  return result

print(fun1(3,3))

def fun2(m,n):
  result = (m**2 - n**2 + n) / (m * n)
  return result

print(fun2(0,0))