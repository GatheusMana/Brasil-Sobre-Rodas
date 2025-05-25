import Grafo as g

caminho = "grafo.txt"

grafo = None

def ler_dados():
    global grafo 
    grafo = g.Grafo()
    grafo.ler_arquivo()
    print("Grafo lido com sucesso!")

def gravar_dados():
    if grafo != None:
            grafo.gravar_em_arquivo()
            print("Grafo salvo com sucesso!")
    else:
        print("Grafo ainda não foi criado!")

def inserir_cidade():
    if grafo != None:
        cidade  = input("Digite o nome da cidade:").strip()
        grafo.adicionar_cidade(cidade)
    else:
        print("Grafo ainda não foi criado!")

def inserir_rota():
    if grafo != None:
        cidade1  = input("Digite o nome da primeira (origem) cidade:").strip()
        cidade2 = input("Digite o nome da segunda (destino) cidade:").strip()
        distancia = input("Digite a distancia entre as cidades:").strip()
        while not distancia.isnumeric():
            distancia = input("Número inválido, digite novamente:").strip()
        while cidade1 == cidade2:
            print("As cidades não podem ser iguais. Digite novamente para continuar:")
            cidade1  = input("Digite o nome da primeira (origem) cidade:").strip()
            cidade2 = input("Digite o nome da segunda (destino) cidade:").strip()
        grafo.inserir_rota(cidade1,cidade2,distancia)        
    else:
        print("Grafo ainda não foi criado!")

def remover_cidade():
    if grafo != None:
        cidade  = input("Digite o nome da cidade:").strip()
        grafo.remover_cidade(cidade)
    else:
        print("Grafo ainda não foi criado!")

def remover_rota():
    if grafo != None:
        cidade1  = input("Digite o nome da primeira (origem) cidade:").strip()
        cidade2 = input("Digite o nome da segunda (destino) cidade:").strip()
        while cidade1 == cidade2:
            print("As cidades não podem ser iguais. Digite novamente para continuar:")
            cidade1  = input("Digite o nome da primeira (origem) cidade:").strip()
            cidade2 = input("Digite o nome da segunda (destino) cidade:").strip()
        grafo.remover_rota(cidade1,cidade2)        
    else:
        print("Grafo ainda não foi criado!")

def exibir_grafo():
    if grafo != None:
        grafo.exibir()
    else:
        print("Grafo ainda não foi criado!")

def exibir_caracteristicas_grafo():
    if grafo != None:
        grafo.exibir_caracteristicas()
    else:
        print("Grafo ainda não foi criado!")

def encontrar_menor_caminho():
    if grafo != None:
        cidade_inicio = input("Digite a cidade de início: ").strip()
        cidade_fim = input("Digite a cidade de destino: ").strip()

        grafo.exibir_menor_caminho(cidade_inicio, cidade_fim)
    else:
        print("Grafo ainda não foi criado!")

def menu():
    while True:
        print("Bem vindo ao Brasil sobre Trilhos")
        print("1 - Ler dados do arquivo grafo.txt")
        print("2 - Gravar dados no arquivo grafo.txt")
        print("3 - Inserir cidade (vértice)")
        print("4 - Inserir rota (aresta)")
        print("5 - Remover cidade (vértice)")
        print("6 - Remover rota (aresta)")
        print("7 - Exibir grafo")
        print("8 - Exibir características do grafo")
        print("9 - Encontrar menor caminho entre duas cidades")
        print("10 - Encerrar")
        
        opc = input("Digite a opção desejada:").strip()
        if opc == '1':
            ler_dados()
        elif opc == '2':
            gravar_dados()
        elif opc == '3':
            inserir_cidade()
        elif opc == '4':
            inserir_rota()
        elif opc == '5':
            remover_cidade()
        elif opc == '6':
            remover_rota()
        elif opc == '7':
            exibir_grafo()
        elif opc == '8':
            exibir_caracteristicas_grafo()
        elif opc == '9':
            encontrar_menor_caminho()
        elif opc == '10':
            print("Programa encerrando...")
            return
        else:
            print("Opção inválida! Digite novamente para continuar")

if __name__ == "__main__":
    menu()
