temp_forno = 0

def preparar_massa():
  print('Preparando a Massa:')
  print('Ingrediantes misturados')
  print('Ingredientes batidos')
  print('Fermento adicionado')
  print('================================')

def untar_forma():
  print('Untando a forma:')
  print('Forma pincelada com manteiga')
  print('Forma polvilhada com farinha')
  print('================================')
  

def ajustar_temperatura_forno():
  global temp_forno
  temp_forno = 200
  print(f'Início - Temperatura do forno ajustada para {temp_forno}ºC.')
  print('================================')
  

def assar_bolo():
  print('Assando o bolo:')
  print('Massa colocada na forma')
  print('Forma levado ao forno')
  
def preparar_cobertura():
  print('Decorando o bolo:')
  print('Cobertura de chocolate finalizada')

def decorar_bolo():
  preparar_cobertura()
  print('Cobertura adicionada ao bolo')
  print('Granulado adicionado ao bolo')

def main():
  pronto_para_assar = False
  
  ajustar_temperatura_forno()
  untar_forma()
  preparar_massa()
  
  while not pronto_para_assar:
    if temp_forno >= 200:
      pronto_para_assar = True
      print(f'Temperatura do forno atingiu 200ºC.')
      print('================================')
      
  assar_bolo()
  
  print('Bolo assado após 20min')
  print('================================')
  
  decorar_bolo()
  
  print('================================')
  print('Fim - Bolo pronto para comer!')

main()
  