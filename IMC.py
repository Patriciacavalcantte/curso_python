#IMC = peso / (altura x altura) 
nome = 'Marcella'
altura = 1.65
peso = 86
IMC = peso / (altura * altura)
IMC_formatado = round(IMC, 1)
if IMC > 25:
    print(nome, "tem", IMC_formatado,"de IMC", "e está gorda!")
 