# Vamos a construir el juego de piedra papel y tijera.

# Nucleo del juego:
def game_loop():
  """
  Arranca el bucle principal del juego
  """
  while True:
    # Leo la seleccion del usuario (piedra, papel, tijera, o parar)
    user_choise = read_user_choise()
    # Siempre y cuando no quiera parar
    if not is_exit(user_choise):
      # genero una jugada del ordenador
      comp_choise = generate_computer_choise()
      #evalua la jugada
      result = evaluate_move(user_choise, comp_choise)
      # muestro el ganador en pantalla y vuelta al principio
      print_result(result)
    else:
      # el humano es gallina: salgo
      break

# Funcion que hace la peticion al usuario:
def read_user_choise():
  """
  Leo la seleccion del usuario (piedra, papel, tijera, o parar) y la devuelvo
  """
  return None

def is_exit(user_choise):
  """
  Predicado que recibe True si el usuario ha decidido parar y False si quiere seguir jugando
  """
  return True

def generate_computer_choise():
  """
  Genera y devuelve una jugada al azar
  """
  return None

def evaluate_move(user_choise, comp_choise):
  """
  Compara las dos jugadas y retorna un texto con el resultado.
  """
  return None

def print_result(result):
  """
  Imprime en bonito el resultado
  """
  return None

# Para llamar el script desde la linea de comando:
if __name__ == "__main__":
  print('Me llama alguien?')
  game_loop()