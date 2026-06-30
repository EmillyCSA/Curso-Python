
# EXERCICIO 7

# Monte um programa que, para um determinado número informado pelo usuário (limite),
# exiba o dobro de cada número de 1 até esse limite.



limite = int (input("Informe o limite: "))

produtorio = 1

for i in range (1, limite + 1):
    produtorio = produtorio * i

print (f"Resultado produtorio: {produtorio}")