"""Calculadora com while"""

#Lógica dos inputs do usuário 
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/ou*): ')

#Lógica de validação - cuidados com o usuário burro#

    numeros_validos = None
    num_2_float = 0
    num_2_float = 0

    try:
        numero_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos: None
    if numeros_validos is None:
        print('Um ou ambos números digitados são inválidos.')
        continue
    
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido!')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador')

  ### lógica dos cálculos ####
    print('Efetuei sua conta. Confira o resultado abaixo:')
    if operador == '+':
      print(numero_1_float + num_2_float )
    elif operador == '-':
        print(numero_1_float - num_2_float )

    elif operador == '/':
        print(numero_1_float / num_2_float )
    elif operador == '*':
        print(numero_1_float * num_2_float )

    #####Encerrando o programa####
    sair = input('Quer sair? [s]im?').lower().startswith('s')
    print(sair)
    
    if sair is True:
        break