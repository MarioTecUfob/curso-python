'''
Docstring para desafio
Você está desenvolvendo um sistema para uma empresa de delivery. O valor da taxa de entrega depende da distância até o cliente e se o pedido foi feito em um dia de chuva.

As regras são:
Para entregas até 5 km, a taxa é R$ 5,00.
Entre 5 e 10 km, a taxa é R$ 8,00.
Acima de 10 km, a taxa é R$ 10,00.
Se estiver chovendo, acrescenta R$ 2,00 à taxa padrão.
O desafio desta atividade é criar um algoritmo que informe o valor final da entrega.
'''
pedido = 'SIM'
while pedido == 'SIM':
    clima = input('Está chovendo? SIM/NÃO ').upper()
    distancia = float(input("Informe a distnacia percorrida km: "))

 # Define a taxa base pela distância
    if distancia <= 5:
        taxa_entrega = 5
    elif 5 < distancia <= 10:
        taxa_entrega = 8
    else:
        taxa_entrega = 10

  # Acrescenta taxa em caso de chuva
    if clima == 'SIM':
         taxa_entrega += 2
         
    print(f'O valor final da taxa de entrega é R$ {taxa_entrega:.2f}')
    pedido = input('Deseja realizar outro pedido? (SIM/NÃO): ').upper()