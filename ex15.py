#Dado N inteiro positivo, dizemos que N é perfeito se for igual à soma de seus divisores
#positivos diferentes de N.
#Exemplo:6 é perfeito, pois 1+2+3=6.
#Verificar se um dado número inteiro positivo é perfeito.

n = int(input("Digite um número inteiro: "))

for i in range(1, n):
    if n % i == 0:
        soma += i

if soma == n:
    print(f"{n} é um número perfeito")
else:
    print(f"{n} não é um número perfeito")