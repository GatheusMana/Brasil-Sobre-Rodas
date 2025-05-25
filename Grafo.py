import heapq
tipos_grafo = {
'0':  "grafo não orientado sem peso",
'1':  "grafo não orientado com peso no vértice",
'2':  "grafo não orientado com peso na aresta",
'3':  "grafo não orientado com peso nos vértices e arestas",
'4':  "grafo orientado sem peso",
'5':  "grafo orientado com peso no vértice",
"6":  "grafo orientado com peso na aresta",
'7':  "grafo orientado com peso nos vértices e arestas"
}


class Rota:
    def __init__(self, origem, destino, distancia):
        self.origem = origem
        self.destino = destino
        self.distancia = distancia

class Cidade:
    def __init__(self, nome):
        self.nome = nome
        self.rotas = []  # Lista de rotas que saem/chegam desta cidade (Arestas)

class Grafo:
    #Construtor
    def __init__(self):
        self.cidades = [] # Conjunto de Cidades(Vértices)
        self.total_cidades = 0 # Quantidade de cidades 
        self.total_rotas = 0 # Quantidade de Rotas (Arestas)
        self.tipo = '' # Tipo do Grafo

    def busca_cidade(self, cidade_alvo):
        for cidade in self.cidades:
            if cidade.nome == cidade_alvo.nome:
                return cidade
        return None
    
    def adicionar_cidade(self, nova_cidade):
        # Cria um novo objeto com a string passada no parâmetro
        nova_cidade = Cidade(nova_cidade)
        # Verifica se existe uma cidade com esse mesmo nome e retorna o objeto caso exista, se não cria o objeto no grafo
        cidade_duplicada = self.busca_cidade(nova_cidade)
        if cidade_duplicada == None:
            self.cidades.append(nova_cidade)
            self.total_cidades += 1
            print(f"{nova_cidade.nome} adicionada ao grafo!")
            return nova_cidade
        else: return cidade_duplicada

    def remover_cidade(self, cidade):
        cidade = self.busca_cidade(Cidade(cidade))
        if cidade != None:
            # Remove esta cidade das rotas de outras cidades
            for rota in cidade.rotas:
                self.remover_rota(rota.origem.nome, rota.destino.nome)
            # Remove a cidade do grafo
            self.cidades.remove(cidade)
            self.total_cidades -= 1
            print(f"Cidade '{cidade.nome}' foi removida do grafo.")
        else:
            print(f"Cidade '{cidade.nome}' não existe no grafo.")
    
    def inserir_rota(self, origem, destino, distancia):
        # Verifica se a cidades de origem e destino já estão no grafo: se tiver trocam os valores se não adicionam
        origem = self.adicionar_cidade(origem)
        destino = self.adicionar_cidade(destino)

        # Adiciona no grafo a "ida" -> Não orientado
        rota = Rota(origem, destino, distancia)
        origem.rotas.append(rota)

        # Adiciona no grafo a "volta" -> Não orientado
        rota_inversa = Rota(destino, origem, distancia)
        destino.rotas.append(rota_inversa)
        self.total_rotas += 1
        print(f"A rota {origem.nome} para {destino.nome} com {distancia} km foi inserida com sucesso!")

    def remover_rota(self, origem, destino):
        origem = self.busca_cidade(Cidade(origem))
        destino = self.busca_cidade(Cidade(destino))
        # Remove da cidade de origem -> Não orientado
        origem.rotas = [r for r in origem.rotas if r.destino != destino]
        # Remove da cidade de destino -> Não orientado
        destino.rotas = [r for r in destino.rotas if r.destino != origem]
        self.total_rotas -= 1
        print(f"A rota {origem.nome} para {destino.nome} foi removida com sucesso!")

    def eh_conexo(self):
        if not self.cidades:
            return True  # Grafo vazio é considerado conexo

        visitadas = set()

        def dfs(cidade):
            visitadas.add(cidade)
            for rota in cidade.rotas:
                if rota.destino not in visitadas:
                    dfs(rota.destino)

        # Começa a busca pela primeira cidade da lista
        dfs(self.cidades[0])

        # Se todas as cidades foram visitadas, é conexo
        if len(visitadas) == len(self.cidades): return "conexo"
        return "não conexo"

    def eh_euleriano(self):
        if self.eh_conexo() != "conexo":
            return False

        vertices_impares = 0
        for cidade in self.cidades:
            grau = len(cidade.rotas)
            if grau % 2 != 0:
                vertices_impares += 1

        return vertices_impares == 0

    def exibir(self):
        print(f"\nGrafo {self.eh_conexo()} do tipo {self.tipo} - {tipos_grafo[self.tipo]}.\nCom {self.total_cidades} cidades e {self.total_rotas} rotas:")
        for cidade in self.cidades:
            print(f"\n{cidade.nome} está ligada a:")
            for rota in cidade.rotas:
                print(f"  -> {rota.destino.nome} ({rota.distancia} km)")
        print("\nFim da impressão do grafo.")

    def exibir_caracteristicas(self):
        print("\n=== Características do Grafo ===")
        
        # Verifica se é conexo
        conexo = self.eh_conexo()
        if conexo == "conexo":
            print("O grafo é CONEXO: Todas as cidades estão interligadas.")
        else:
            print("O grafo NÃO é conexo: Existem cidades isoladas ou desconectadas.")

        # Verifica se é euleriano
        euleriano = self.eh_euleriano()
        if euleriano:
            print("O grafo é EULERIANO: É possível percorrer todas as rotas sem repetição.")
        else:
            print("O grafo NÃO é euleriano: Não é possível percorrer todas as rotas sem repetição.")

    def ler_arquivo(self):
        arquivo = open("grafo.txt", "r", encoding='utf-8')
        
        # Recebendo e atribuindo o tipo do grafo conforme padrão do arquivo
        tipoGrafo = arquivo.readline().strip()
        self.tipo = tipoGrafo

        # Recebendo e atribuindo quantidade de cidades
        total_cidades = int(arquivo.readline().strip())
        # Recebendo as cidades do arquivo
        for i in range(total_cidades):
            cidade = arquivo.readline().strip()
            self.adicionar_cidade(cidade)

        # Recebendo e atribuindo quantidade de rotas
        total_rotas = int(arquivo.readline().strip())
        # Recebendo as rotas do arquivo
        for i in range(total_rotas):
            linha = arquivo.readline().strip()
            dados = linha.split(";")
            origem, distancia, destino = dados[0].strip(), int(dados[1]), dados[2].strip()
            self.inserir_rota(origem, destino, distancia)
        
        # Fechando o arquivo
        arquivo.close()
        
    def gravar_em_arquivo(self):

        try:
            with open("grafo.txt", "w", encoding="utf-8") as arquivo:

                arquivo.write(f"{self.tipo}\n")

                # Número de cidades
                arquivo.write(f"{self.total_cidades}\n")

                # Lista de cidades
                for cidade in self.cidades:
                    arquivo.write(f"{cidade.nome}\n")

                # Lista de rotas (evitando duplicatas)
                rotas_gravadas = set()
                todas_rotas = []

                for cidade in self.cidades:
                    for rota in cidade.rotas:
                        par = tuple(sorted([rota.origem.nome, rota.destino.nome]))
                        if par not in rotas_gravadas:
                            rotas_gravadas.add(par)
                            todas_rotas.append(f"{rota.origem.nome};{rota.distancia};{rota.destino.nome}")

                # Número de rotas
                arquivo.write(f"{self.total_rotas}\n")

                # Grava cada rota
                for linha in todas_rotas:
                    arquivo.write(linha + "\n")

        except Exception as e:
            print(f"Erro ao gravar o arquivo: {e}")

    def dijkstra(self, inicio_nome, fim_nome):
        # Busca os objetos Cidade
        inicio = self.busca_cidade(Cidade(inicio_nome))
        fim = self.busca_cidade(Cidade(fim_nome))

        if not inicio or not fim:
            print("Uma ou ambas as cidades não foram encontradas no grafo.")
            return [], float('inf')

        # Inicializa distâncias e predecessores
        distancias = {cidade: float('inf') for cidade in self.cidades}
        predecessores = {cidade: None for cidade in self.cidades}
        distancias[inicio] = 0

        # Fila de prioridade: (distância, nome da cidade)
        fila = [(0, inicio.nome)]  # Usamos o nome da cidade aqui

        visitadas = set()

        while fila:
            distancia_atual, nome_atual = heapq.heappop(fila)
            cidade_atual = self.busca_cidade(Cidade(nome_atual))

            if cidade_atual in visitadas:
                continue

            visitadas.add(cidade_atual)

            if cidade_atual == fim:
                break

            for rota in cidade_atual.rotas:
                vizinho = rota.destino
                nova_distancia = distancia_atual + int(rota.distancia)

                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = cidade_atual
                    heapq.heappush(fila, (nova_distancia, vizinho.nome))  # Usamos o nome novamente

        # Reconstrói o caminho
        caminho = []
        atual = fim
        if distancias[atual] == float('inf'):
            return [], float('inf')  # Caminho não existe

        while atual:
            caminho.insert(0, atual.nome)
            atual = predecessores[atual]

        return caminho, distancias[fim]

    def exibir_menor_caminho(self, inicio, fim):
        caminho, distancia = self.dijkstra(inicio, fim)
        if not caminho:
            print(f"\nNão há caminho entre '{inicio}' e '{fim}'.")
        elif distancia == float('inf'):
            print(f"\n'{fim}' não é alcançável a partir de '{inicio}'.")
        else:
            print(f"\nMenor caminho de '{inicio}' até '{fim}':")
            print(" → ".join(caminho))
            print(f"Distância total: {distancia} km")
