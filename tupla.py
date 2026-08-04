tupla = (10 , 20 , 30 , 40)

print (f"Tipo da tupla: {type(tupla)}")
print (tupla)


lista_convertida = list(tupla)

print (f"Tipo de lista_convertida: {type(lista_convertida)}")

lista_convertida [2]= 300

tupla_convertida = tuple(lista_convertida)

print (tupla_convertida)