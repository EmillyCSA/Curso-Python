idade = int(input("Informe a idade:"))

if idade < 6:
    print ("Tarifa gratuita.")
elif (idade >= 6) and (idade < 18):
    print ("Tarifa R$5.")
elif (idade >= 18) and (idade < 60):
    print ("Tarifa R$10.")
else:
    print ("Tarifa gratuita.")