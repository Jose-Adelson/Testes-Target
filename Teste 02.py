Num_A = 0
Num_B = 1
I = 0 #contador

S = int(input("Quantos termos você quer que possua a sequência de Fibonacci? "))
N = int(input("Digite um número: "))
L = [0,1] #Sequência de Fibonacci

while I <= S:
    Num_C = Num_A + Num_B
    Num_A = Num_B
    Num_B = Num_C
    I += 1
    L.append(Num_C)
   
print(L)   
if N in L:
    print("O número informado pertence a sequência de Fibonacci!")
else:
    print("O número informado não pertence a sequência de Fibonacci!")