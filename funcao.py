'''
Docstring: Programa que converte temperatura de Celsius (°C) para Fahrenheit (°F).

#Entrada:
    Valor da temperatura em graus Celsius.
   
#Processamento
    Fahrenheit = (celsius *9/5)+32

#Saída
    Temperatura convertida em graus Fahrenheit.

'''
#FUNÇÃO: Bloco de algoritmo que realiza uma tarefa específica. Recebe entrada (parâmetros) e devolve saídas (retornos)
#Exemplo: f(x) = ax + b → para cada valor de x do domínio, a função retorna um valor y, que pertence à imagem.


def ConverterCparaF(celsius):
    return (celsius * 9/5) + 32

temperatura = float(input("Digite a temperatura em Celsius: "))
resultado = ConverterCparaF(temperatura)

print(f"O valor da temperatura em Fahrenheit é {resultado:.1f} °F")

'''
Você está desenvolvendo um sistema de apoio para uma agência de viagens. Uma das funcionalidades mais solicitadas é um conversor de moedas.
 O usuário informa um valor em reais (R$) e o sistema precisa mostrar quanto isso representa em dólares (US$), usando uma taxa de câmbio definida pela empresa.

Sua tarefa é criar um algoritmo que use uma função para fazer essa conversão. A função deve receber o valor em reais e a taxa de câmbio como entrada, e retornar o valor convertido.
'''
def Converter_para_dolar(valor_em_reais,taxa_cambio):
    return (valor_em_reais/taxa_cambio)
#Entrada
valor = float(input('informe o valor em reais (R$): '))
taxa = 5.29
#Processamento
valor_convertido = Converter_para_dolar(valor,taxa)
#Saída
print (f'R$ {valor:.2f} coresponde a US$ {valor_convertido:.2f}')

'''Você foi contratado por uma cafeteria que deseja automatizar o atendimento no balcão.
 O sistema deve permitir que o atendente registre os pedidos de cada cliente, calcule o valor total e aplique um desconto de 10% para clientes cadastrados.

O processo deve funcionar da seguinte forma:

O atendente informa quantos itens o cliente vai pedir.
Para cada item, o sistema solicita o nome e o preço.
Ao final, o sistema pergunta se o cliente é cadastrado.
Se for, aplica o desconto e exibe o valor com desconto.
Caso contrário, exibe o valor cheio.
O desafio consiste em criar um algoritmo que represente essa lógica de forma completa.
'''