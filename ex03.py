#Deseja-se fazer um levantamento a respeito da ausência de alunos à primeira prova de
#Programação de Computadores para cada uma das 14 turmas existentes. Para cada turma é
#fornecido um conjunto de valores, sendo que os dois primeiros valores do conjunto
#correspondem à identificação da turma (A, ou B, ou C, ...) e ao número de alunos
#matriculados, e os demais valores deste conjunto contêm o número de matrícula do aluno e a
#letra A ou P para o caso de o aluno estar ausente ou presente, respectivamente. Fazer um
#algoritmo que:
#- para cada turma, calcule a porcentagem de ausência e escreva a identificação da turma e
#a porcentagem calculada;
#- determine e escreva quantas turmas tiveram porcentagem de ausência superiora5%.

dados_turma = []
acima_5 = 0

while True:
    turma = input("Lista de presença da turma: ")
    num_aluno = int(input(f"Qual é o número de alunos matriculados na turma {turma}: "))

    faltas, presente = 0, 0

    for i in range(num_aluno):
        print("-"*40)
        matri = input("Número da matrícula: ")
        presenca = input("Ausente (A) ou Presente (P): ").upper()

        if presenca == "A":
            faltas += 1
        elif presenca == "P":
            presente += 1

    porcentagem = (faltas / num_aluno) * 100

    dados_turma.append([turma, presente, faltas, porcentagem])

    if porcentagem > 5:
        acima_5 += 1

    continuar = input("\nDeseja fazer a chamada de outra turma? (S/N): ").upper()

    if continuar != "S":
        break


print("\nPorcentagem de ausência por turma")
for turma, presente, faltas, porcentagem in dados_turma:
    print(f"Turma: {turma} | Presentes: {presente} | Ausentes: {faltas} | Porcentagem de Ausências: {porcentagem:.2f}%")

print("-"*40)
print(f"Quantidade de turmas com ausência superior a 5%: {acima_5}")








