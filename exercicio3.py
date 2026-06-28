
#EXERCICIO 3

#Peça ao usuário para digitar um username e uma senha.
#Considere que o usuário correto é "admin" e que a senha correta é python2026.
#Se as credencias estiverem corretas, exiba "Login bem sucedido!".
#Do contrário, exiba que as credenciais estão incorretas.


username_correto = "admin"
senha_correta = "python2026"

username_entrada = (input("username: "))
senha_entrada = (input("senha: "))

if (username_entrada == username_correto) and (senha_entrada == senha_correta):
    print ("Login bem sucedido!")
else:
    print ("Credenciais incorretas.")