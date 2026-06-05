#Dado um número inteiro positivo N, determinar todos os inteiros entre 1 e N que são
#comprimento de hipotenusa de um triângulo retângulo com catetos inteiros.

n = int(input("Digite N: "))

print("Hipotenusas entre 1 e", n)

for c in range(1, n + 1):

    encontrou = False

    for a in range(1, c):
        for b in range(1, c):

            if a**2 + b**2 == c**2:
                encontrou = True
                break

        if encontrou:
            break

    if encontrou:
        print(c)