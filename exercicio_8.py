# EXERCICIO 9 

# Monte um programa que, para um determinado número informado pelo usuário (limite),
# exiba o dobro de cada número de 1 até esse limite.
# 
# 
# Exemplo de entrada:4
# Exemplo de saída:
# Dobro de 1: 2
# Dobro de 2: 4
# Dobro de 3: 6
# Dobro de 4: 8 

limite = int (input("Informe o limite:"))

for i in range (1, limite + 1):
    print(f"Informe o dobro {i}: {i * 2}")