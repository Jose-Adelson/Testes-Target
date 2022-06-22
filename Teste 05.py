palavra = input("Digite uma palavra: ")
palavra_inversa =""

contador = len(palavra)
while contador:
        contador = contador - 1                 
        palavra_inversa = palavra_inversa + palavra[contador] 
    
print(palavra_inversa)