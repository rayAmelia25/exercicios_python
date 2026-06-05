#Escreva um algoritmo que leia e mostre um texto, caracter a caracter, até encontrar a seqüência
#de caracteres "/*", que determina o final do texto.
print("Digite um texto (finalize com /*):")
anterior = ""
while True:
    texto = input()
    
    if (anterior == "/") and (texto == "*"):
        print("finaliza porra")
        break
    if anterior != "":
        print(anterior, end="")

    anterior = texto


        
print("acabou?")


