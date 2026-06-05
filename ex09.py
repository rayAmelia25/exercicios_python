#Escreva um algoritmo que leia um número inteiro, positivo N, calcule e mostre o maior
#quadrado menor ou igual a N. Por exemplo, se N for maior ou igual a 38, o menorquadrado é
#36 (quadrado de 6).

n = int(input("Digite um número inteiro: "))
i = 1

while i*i <= n:
    quadrado = i * i
    i += 1
    
print(f"O maior quadrado menor ou igual a {n}, é {quadrado}.")