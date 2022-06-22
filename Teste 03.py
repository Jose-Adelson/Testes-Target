import json

dados = open("dados.json")
lista = json.load(dados)

def menor_valor():
    menorvalor = 10000000000000000
    for i in lista:
        if i["valor"] > 0 and i["valor"] < menorvalor:
            menorvalor = (i["valor"])
            dia = i["dia"]
    print("No dia %s foi o menor valor de faturamento ocorrido do mês, que foi de R$:%f " %(dia,menorvalor)) 

def maior_valor():
    maiorvalor = 0
    for i in lista:
        if i["valor"] > maiorvalor:        
            maiorvalor = (i["valor"])
            dia = i["dia"]      
    print("No dia %s foi o maior valor de faturamento ocorrido do mês, que foi de R$:%f " %(dia,maiorvalor)) 

def media():
    soma = 0
    divisor = 0
    media = 0
    ndias = 1
    for i in lista:
        if i["valor"] > 0:
            soma = soma + i["valor"]
            divisor = divisor + 1
        media = soma/divisor
        if i["valor"] > media:
            ndias = ndias + 1

    print("A média mensal é de R$%.2f, e %d foi o Número de dias no mês em que o valor de faturamento diário foi superior à média mensal" %(media,ndias))

media()
menor_valor()
maior_valor()