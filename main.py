import math 

print("O programa a seguir tem como intuito determinar resultados de contas relacionadas ao estudo da polarização da luz. É requerível que o usuário tenha uma boa interpretação dos problemas relacionados a polarização da luz para utilização correta da aplicação. Neste código conseguimos determinar intensidade da luz não polarizada, intensidade da luz após passar por um conjunto, intensidade da luz incidente e intensidade da luz passando por até dois filtros polarizadores. Em alguns casos também podemos descobrir a intensidade da luz antes de passar pelo polarizador ou antes de passar por um filtro.")

def menu():

  print("""
      1 - Intensidade da luz com dois filtros.
      2 - Intensidade da luz com dois filtros após atravessar o primeiro filtro.
      3 - Intensidade da luz com dois filtros após atravessar o conjunto.
      4 - Intensidade da luz com três filtros. (2 ângulos)
      5 - Intensidade da luz com três filtros a partir do primeiro polarizador. 
      (2 ângulos)
      6 - Intensidade da luz com três filtros a partir do segundo polarizador. 
      (2 ângulos)
      7 - Intensidade da luz com três filtros a partir do conjunto.
      (2 ângulos)
      8 - Intensidade com apenas um filtro.
      0 - Sair
      
      
      Desenvolvido por: Stella de Oliveira e Luis Marim 
  """)


def escolha():
  print('\n')
  A = int(input('Escolha uma opção: '))
  print('\n')
  return A


def sair():
  print('Você saiu !')


def intensidade():
  
  print('Intensidade da luz')
  print('\n')
  i0 = float(input("Intensidade da luz não polarizada: "))
  angulo = float(input("Ângulo: "))
  ang_rad = math.radians(angulo)
  print('\n')

  primeiro_filtro = i0/2
  arredonda = round(primeiro_filtro, 2)
  conjunto = arredonda * math.cos(ang_rad-0)**2

  print(f'Intensidade do primeiro filtro polarizador [W/cm^2]: {arredonda:.4e}')
  print('\n')
  print(f'A intensidade da luz após ela ter atravessado o conjunto é [W/cm^2]: {conjunto:.4e}')
  print("\n")

def intensidade_primeiro_filtro():
  print('Intensidade da luz')
  print('\n')
  i0 = float(input("Intensidade da luz não polarizada: "))
  angulo = float(input("Ângulo: "))
  ang_rad = math.radians(angulo)
  print('\n')
  
  i0_incidente = i0*2
  conjunto_incidente = i0 * math.cos(ang_rad-0)**2

  print(f"Intensidade da luz incidente [W/cm^2]: {i0_incidente :.4e}")
  print("\n")
  print(f'A intensidade da luz após ela ter atravessado o conjunto (LUZ INCIDENTE) é [W/cm^2]:  {conjunto_incidente:.4e}')

def intensidade_conjunto():
  print('Intensidade da luz')
  print('\n')
  i0 = float(input("Intensidade da luz: "))
  angulo = float(input("Ângulo: "))
  ang_rad = math.radians(angulo)
  print('\n')
  i2 = (i0/2)*math.cos(ang_rad)**2
  i0_0 = (2*i2)/math.cos(ang_rad)**2
  i = (2*i0_0)/math.cos(ang_rad)**2
  primeiro_filtro = i/2
  print(f"Intensidade da luz incidente [W/cm^2]: {i:.4e}")
  print('\n')
  print(f'Intensidade do primeiro filtro polarizador [W/cm^2]: {primeiro_filtro:.4e}')

def intensidade_angulos():
  print('Intensidade da luz')
  print('\n')
  i0 = float(input("Intensidade da luz: "))
  angulo1 = float(input("Menor Ângulo: "))
  ang_rad = math.radians(angulo1)
  angulo2 = float(input("Maior Ângulo: "))
  ang_rad2 = math.radians(angulo1)
  i1 = i0/2
  i2 = i1*math.cos(ang_rad)**2
  apoio = angulo2 - angulo1
  apoio_rad = math.radians(apoio)
  i3 = i2*math.cos(apoio_rad)**2
  print(f"A intensidade da luz depois de passar pelo primeiro polarizador [W/cm^2]: {i1:.4e}")
  print('\n')
  print(f"A intensidade da luz depois de passar pelo segundo polarizador [W/cm^2]: {i2:.4e}")
  print('\n')
  print(f"A intensidade da luz depois de passar pelo conjunto [W/cm^2]: {i3:.4e}")
  
def intensidade_angulosPrimeiro():
  print('Intensidade da luz')
  print('\n')
  i0 = float(input("Intensidade da luz não polarizada: "))
  angulo1 = float(input("Menor Ângulo: "))
  ang_rad = math.radians(angulo1)
  angulo2 = float(input("Maior Ângulo: "))
  ang_rad2 = math.radians(angulo1)
  i1 = 2.0*i0
  i2 = i0*math.cos(ang_rad)**2
  apoio = angulo2 - angulo1
  apoio_rad = math.radians(apoio)
  i3 = i2*math.cos(apoio_rad)**2
  print(f"Intensidade da luz incidente [W/cm^2]: {i1:.4e}")
  print("\n")
  print(f"A intensidade da luz após ela ter atravessado o segundo polarizador [W/cm^2]: {i2:.4e}")
  print("\n")
  print(f"A intensidade da luz depois de passar pelo conjunto [W/cm^2]: {i3:.4e}")

def intensidade_angulosSegundo():
  print('Intensidade da luz')
  print('\n')
  i0 = float(input("Intensidade da luz não polarizada: "))
  angulo1 = float(input("Menor Ângulo: "))
  ang_rad = math.radians(angulo1)
  angulo2 = float(input("Maior Ângulo: "))
  ang_rad2 = math.radians(angulo1)
  print('\n')
  i2 = (i0/2)*math.cos(ang_rad)**2
  i0_0 = (2*i2)/math.cos(ang_rad)**2
  i = (2*i0_0)/math.cos(ang_rad)**2
  primeiro_filtro = i/2
  apoio = angulo2 - angulo1
  apoio_rad = math.radians(apoio)
  i3 = i0_0*math.cos(apoio_rad)**2
  print("Intensidade da luz incidente [W/cm^2]: ", i)
  print("\n")
  print(f"A intensidade da luz depois de passar pelo primeiro polarizador [W/cm^2]: {primeiro_filtro:.4e}")
  print("\n")
  print(f"A intensidade da luz depois de passar pelo conjunto [W/cm^2]: {i3:.4e}")

def intensidade_angulosConjunto():
  print('Intensidade da luz')
  print('\n')
  i0 = float(input("Intensidade da luz: "))
  angulo1 = float(input("Menor Ângulo: "))
  ang_rad = math.radians(angulo1)
  angulo2 = float(input("Maior Ângulo: "))
  ang_rad2 = math.radians(angulo1)
  apoio = angulo2 - angulo1
  apoio_rad = math.radians(apoio)
  print('\n')
  i = (2*i0)/(math.cos(ang_rad)**2)/(math.cos(apoio_rad)**2)
  i1 = i/2
  i2 = i1*math.cos(ang_rad)**2
  print("Intensidade da luz incidente [W/cm^2]: ", i)
  print("\n")
  print(f"A intensidade da luz após ela ter atravessado o segundo polarizador [W/cm^2]: {i1:.4e}")
  print("\n")
  print(f"A intensidade da luz depois de passar pelo primeiro polarizador [W/cm^2]: {i2:.4e}")

def umFiltro():
  print('Intensidade da luz')
  print('\n')
  i0 = float(input("Intensidade da luz antes de passar pelo polarizador: "))
  i1 = i0/2
  i2 = float(input("Intensidade da luz depois de passar pelo polarizador: "))
  i3 = i2*2
  print('\n')
  print(f"A intensidade da luz após ela ter atravessado o filtro [W/cm^2]: {i1:.4e}")
  print('\n')
  print(f"A intensidade da luz antes dela ter atravessado o filtro [W/cm^2]: {i3:.4e}")
  
  


while True:

  menu()

  x = escolha()

  if (x == 1):
    intensidade()

  if (x == 2):
    intensidade_primeiro_filtro()

  if (x == 3):
    intensidade_conjunto()

  if (x==4):
    intensidade_angulos()

  if (x==5):
    intensidade_angulosPrimeiro()

  if (x == 6):
    intensidade_angulosSegundo()

  if (x==7):
    intensidade_angulosConjunto()

  if (x ==8):
    umFiltro()

  if (x == 0):

    sair()
    break
