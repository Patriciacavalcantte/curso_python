"""
Peça ao usuário para digitar seu nome 
Peça ao usuário para digitar sua idade 
Se nome e idade forem digitados:
  Exiba:
    seu nome é {nome}
    seu nome é {nome invertido}
    Seu nome contém (ou não) e espaços 
    Seu nome tem {n} letras
    A primeira letra do seu nome é {letra}
    A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
   exiba "Desculpe, você deixou campos vazios."
"""
nome_usario = input('Digite o seu nome: ')
idade_usuario = input("Digite a sua idade: ")
if nome_usario and idade_usuario:
    print(f"Seu nome é {nome_usario}")
    print(f'Seu nome invertido é {nome_usario[::-1]}')

    if ' ' in nome_usario:
        print('Seu nome contém espaços')
    else: 
        print("Seu nome NÃO contém espaços")

    print(f"Seu nome tem {len(nome_usario)} letras")
    print(f"A primeira letra do seu nome é {nome_usario[0]}")
    print(f"A última letra do seu nome é {nome_usario[-1]}")
else:
    print("Desculpe, você deixou campos vazios ")
