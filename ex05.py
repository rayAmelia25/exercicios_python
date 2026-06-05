#Escreva um algoritmo que leia dois números X e N. A seguir, mostre o resultado das divisões
#de X por N, onde, após cada divisão, X passa a ter como conteúdo o resultado da divisão
#anterior e N é decrementado de 1 em 1, até chegar a 2.

X = int(input("Digite o número: "))
N = int(input("Digite outro número: "))

while N > 2:
    div = X / N
    print("Resultado: ", div)
    X = div
    N -= 1

