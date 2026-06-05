#Supondo que a população de um país A seja da ordem de 90.000.000 de habitantes com uma
#taxa anual de crescimento de 3% e que a população de um país B seja,aproximadamente, de
#200.000.000 de habitantes, com uma taxa anual de crescimento de 1,5%, fazer um algoritmo
#que calcule e escreva o número de anos necessários para que a população do país A ultrapasse
#ou iguale a população do país B, mantidas essas taxas de crescimento.

def cresc (popul, taxa):
    return popul + (popul * taxa / 100) 

A = 90000000
B = 200000000
ano = 0

while A < B:
    A = cresc(A, 3)
    B = cresc(B, 1.5)
    ano += 1

print(f"O País A precisa de {ano} anos para ultrapassar ou igualar ao País B")
print(f"População: \nPaís A: {int(A):,}\nPaís B: {int(B):,}".replace(",", "."))

