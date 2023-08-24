#for: utiliza-se quando sabe a quantidade iterável 

#texto = 'Python'

#for letra in texto:
   # print(letra)

"""
For + Range
range -> range(start, stop, step)
"""
'''numeros = range(0, 100, 2)

for numero in numeros:
    print(numero)'''

'''texto = iter('Patricia') #_iter_()
print(next(texto)) #itera e mostra na tela as letras da string'''

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')
