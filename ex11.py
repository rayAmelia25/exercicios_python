#Escreva um algoritmo que leia uma lista de letras terminada pela letra "z". Ao final,o algoritmo
#deve mostrar a quantidade lida de cada vogal.

vogais = ["a", "e", "i", 'o', "u"]
qtd = []

for i in range(5):
    qtd.append(0)

letra = input("Digite as vogais (ou 'z' para sair): ")

while letra.lower() != "z":
   
    for i in range(5):
        if letra == vogais[i]:
            qtd[i] += 1
    
    letra = input("Digite a vogais (ou 'z' para sair): ")

print("\n==========CÁLCULO DAS VOGAIS=============")
for i in range(5):
   print("-"*40)
   print(f"Quantidade de {vogais[i]}: {qtd[i]}")
   