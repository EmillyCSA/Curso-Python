
# EXERCICIO 6

# Monte um programa que peça, um de cada vez, vários números para o usuário
# até que ele digite zero (0). Ao fim, mostre a soma de todos esses números que
# ele digitou.

numero = int (input("Digite um numero: "))

somatorio = 0

while numero != 0:
    somatorio = somatorio + numero
    numero = int (input("Mais um número: "))

print (f"Somatorio dos número: {somatorio}")

