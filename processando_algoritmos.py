'''Algoritmo para verificar meia entrada'''
#Dados de entrada
idade = int(input("Informa a sua idade: ")) 
estudante = input("Você é estudante? SIM/NÃO ").upper()
preco_total = 40
#Processamento
if idade <18 or estudante == 'SIM':
    preco = preco_total/2
    print (f"Meia entrada aplicada")
else:
    preco = preco_total
#Output(Dados de saída)
print (f"valor a ser pago R$ {preco} ")