n = int(input("Quantidade de números: "))

anterior = int(input("Número: "))

atual = 1
maior = 1

for i in range(n - 1):
    num = int(input("Número: "))

    if num > anterior:
        atual += 1
    else:
        atual = 1

    if atual > maior:
        maior = atual

    anterior = num

print("Comprimento do maior segmento crescente:", maior)