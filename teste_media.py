#Praticando - Teste de Média de Aluno.

media = float (input("Média do aluno:"))

if media >=7.0:
    print ("Aprovado!")
elif (media >= 4) and (media <7):
    print ("Recuperação.")

    nota_recuperação = float (input("Nota de recuperação:"))

    if nota_recuperação >=7.0:
        print ("Passou na recuperação!")
    else:
        print("Reprovado na recuperação.")
else:
    print ("Reprovou direto.")
