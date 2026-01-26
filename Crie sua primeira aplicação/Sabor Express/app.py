#O type mostra os tipos de dado, da variável
'''
print(type(opcao_escolhida))
print(type(1))
'''
import os
#A lista armazena uma coleção de dados
restaurantes = [ #Dcionário tem chave(kay) e valor
    {'nome':'Praça','categoria':'Japonesa','ativo':False},
    {'nome':'Pizza Suprema','categoria':'Intaliana','ativo':True},
    {'nome':'Cantina da Serra','categoria':'Baiana','ativo':False}
    ]

def exibir_nome_do_programa():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n''')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('1. Sair\n')

def finalizar_app():
    exibir_subtitulo('𝙁𝙞𝙣𝙖𝙡𝙞𝙯𝙖𝙣𝙙𝙤 𝙤 𝙖𝙥𝙥')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha ='*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''
    Docstring para cadastrar_novo_restaurante
    Função responsável por cadastrar novo restaurante

    Inputs:
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
    exibir_subtitulo('𝘾𝙖𝙙𝙖𝙨𝙩𝙧𝙤 𝙙𝙚 𝙣𝙤𝙫𝙤𝙨 𝙧𝙚𝙨𝙩𝙖𝙪𝙧𝙖𝙣𝙩𝙚𝙨')
    nome_do_restuarante = input('Digite o nome do restuarante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restuarante}: ')
    dados_do_restaurante = {'nome': nome_do_restuarante, 'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restuarante} foi 🇨​​​​​🇦​​​​​🇩​​​​​🇦​​​​​🇸​​​​​🇹​​​​​🇷​​​​​🇦​​​​​🇩​​​​​🇴​​​​​ 🇨​​​​​🇴​​​​​🇲​​​​​ 🇸​​​​​🇺​​​​​🇨​​​​​🇪​​​​​🇸​​​​​🇸​​​​​🇴​​​​!​ 👌')
    voltar_ao_menu_principal()

def listar_restaurantes():    
    exibir_subtitulo('𝐋𝐢𝐬𝐭𝐚𝐧𝐝𝐨 𝐨𝐬 𝐫𝐞𝐬𝐭𝐚𝐮𝐫𝐚𝐧𝐭𝐞𝐬')
    print(f"{'Nome do restautante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativo' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}' )
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('𝘼𝙡𝙩𝙚𝙧𝙣𝙖𝙣𝙙𝙤 𝙚𝙨𝙩𝙖𝙙𝙤 𝙙𝙤 𝙧𝙚𝙨𝙩𝙖𝙪𝙧𝙖𝙣𝙩𝙚')
    nome_do_restuarante = input('Digite o nome do restuarante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_do_restuarante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_do_restuarante} foi ativado com 𝚂𝚄𝙲𝙴𝚂𝚂𝙾! ✅' if restaurante['ativo'] else f'O restaurante {nome_do_restuarante} foi desativado com 𝚂𝚄𝙲𝙴𝚂𝚂𝙾! ✘'
            print(mensagem)
    if not restaurante_encontrado:
        print('\nO restuarante não foi encontrado ( ˘︹˘ )')
    voltar_ao_menu_principal()

#Uso de Snake case conhecido como underscore case padrão para nonomear variáveis, funções e métodos
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
    
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

#Função que controla o projeto 
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()