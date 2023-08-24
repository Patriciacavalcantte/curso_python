"""
OPERADORES LÓGICOS:

and (e) or (ou) not (não)
and - Todas as condições precisam ser verdadeiras 
ou - se qualquer condição for verdadeira a
not - se qualquer valor for c onsiderado falso, a expressão inteira será avaliada naquele valor
São considerados falsy 0 0.0 '' (string vazia) e false 
Também existe o tipo None que é usado para representar um não valor 
"""
"""entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('senha: ')

senha_permitida = '123456'
# if condição, só é executado qdo a expressão é true
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
    """
#avaliação de curto circuito: 
#senha = input('Senha: ') or 'Sem senha'
#print(senha)
#----------------------------------------------------#
#Operador lógico 'not'
#Usado para inverter expressões
# not True = False 
# not False = True
##senha = input('Senha: ')

#if senha != '123456':
    #print('Senha incorreta.')

#if not senha:
    #print('Você não digitou nada')

#operadores in e not - string iteraveis 
"""nome = 'Patricia'
print(nome[2])
print('a' in nome)
print('z' in nome)
print('tricia'not in nome)
print('vio' not in nome)
"""
