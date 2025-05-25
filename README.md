# 🚆 Brasil sobre Trilhos: Mobilidade Sustentável e Conectividade entre Cidades

> Um projeto de modelagem computacional de uma rede ferroviária interligando cidades brasileiras, com o objetivo de simular rotas otimizadas e promover a conscientização sobre os benefícios ambientais e logísticos do transporte ferroviário.

---

## 📌 Autores

- Bruno Burghi Machado – RM 10419527  
- Lauralice de Souza Silva – RM 10416542  
- Matheus Nascimento Gana – RM 10417400  

Universidade Presbiteriana Mackenzie  
Disciplina: Teoria dos Grafos  
Professor: André Rodrigues de Oliveira  
Ano: 2025

---

## 🧩 Descrição do Projeto

Este projeto propõe a criação de uma **simulação de uma malha ferroviária nacional** utilizando **grafos computacionais**, com o objetivo de:

- Modelar conexões entre cidades importantes do Brasil.
- Simular rotas ferroviárias otimizadas com base em distâncias reais.
- Estudar a conectividade entre regiões urbanas e rurais.
- Promover alternativas sustentáveis ao transporte rodoviário.

A implementação foi feita em **Python**, com persistência de dados via arquivo texto e interface interativa no terminal. O projeto utiliza técnicas avançadas de análise de grafos, como o algoritmo de Dijkstra, verificação de conexidade e eulerianidade.

---

## 🛠️ Funcionalidades Implementadas

| Funcionalidade | Descrição |
|----------------|-----------|
| **Leitura do grafo** | Lê o grafo salvo em `grafo.txt` |
| **Gravação do grafo** | Salva alterações no grafo para persistência |
| **Inserção de cidades** | Adiciona novos vértices (cidades) ao grafo |
| **Inserção de rotas** | Adiciona arestas com peso (distância em km) |
| **Remoção de cidades** | Remove cidade e todas rotas associadas |
| **Remoção de rotas** | Remove apenas a ligação entre duas cidades |
| **Exibição do grafo** | Mostra todos os nós e suas ligações |
| **Exibir características do grafo** | Verifica se é **conexo** ou **euleriano** |
| **Menor caminho entre duas cidades** | Encontra rota mínima usando o **algoritmo de Dijkstra** |

---

## 🔍 Principais Algoritmos Utilizados

### 1. **Busca em Profundidade (DFS)**  
**Finalidade:** verificar se o grafo é conexo.  
**Contextualização:** ajuda a identificar se todas as cidades estão interligadas ou se existem áreas isoladas.

```python
def eh_conexo(self):
    ...
```

### 2. **Verificação de Eulerianidade**  
**Finalidade:** verificar se o grafo permite percorrer todas as rotas sem repetição.  
**Contextualização:** útil para planejar rotas de manutenção ou inspeção ferroviária.

```python
def eh_euleriano(self):
    ...
```

### 3. **Algoritmo de Dijkstra**  
**Finalidade:** encontrar o menor caminho entre duas cidades.  
**Contextualização:** essencial para simular rotas otimizadas entre cidades, reduzindo custos e emissões de CO₂.

```python
def dijkstra(self, inicio_nome, fim_nome):
    ...
```

---

## 📁 Estrutura do Projeto

```
Brasil-Sobre-Trilhos/
├── Grafo.py              # Definição das classes e métodos do grafo
├── Main.py               # Menu interativo e controle do usuário
├── grafo.txt             # Arquivo de persistência do grafo
└── README.md             # Este arquivo
```

---

## 📄 Exemplo de Estrutura do Arquivo `grafo.txt`

```
2
3
São Paulo
Rio de Janeiro
Curitiba
3
São Paulo;430;Rio de Janeiro
São Paulo;420;Curitiba
Curitiba;300;Rio de Janeiro
```

- Linha 1: tipo do grafo (ex: 2 = não orientado com peso nas arestas)
- Linha 2: número de cidades
- Próximas linhas: nomes das cidades
- Linha seguinte: número de rotas
- Próximas linhas: rotas no formato `origem;distancia;destino`

---

## 🌱 Objetivos de Desenvolvimento Sustentável (ODS)

Este projeto contempla os seguintes ODS da Agenda 2030 da ONU:

| ODS | Descrição |
|-----|-----------|
| **9** | Indústria, Inovação e Infraestrutura |
| **11** | Cidades e Comunidades Sustentáveis |
| **13** | Ação contra a Mudança Global do Clima |

---

## 📌 Como Executar o Projeto

### Requisitos:
- Python 3.x instalado
- Editor de texto ou IDE (VSCode, PyCharm, etc.)

### Passos:
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/Brasil-Sobre-Trilhos.git
   ```
2. Execute o programa:
   ```bash
   python Main.py
   ```

---

## 📚 Referências

- Organização das Nações Unidas no Brasil – [Objetivos de Desenvolvimento Sustentável](https://brasil.un.org/pt-br/sdgs)
- Railway Association of Canada – [Quarterly Report Q1 2024](https://www.railcan.ca/wp-content/uploads/2024/02/2024_Q1_RAC_Quarterly_Report_EN.pdf)

---

## 📎 Apêndice

- Código fonte completo disponível no repositório:  
  👉 [GitHub - Brasil Sobre Trilhos](https://github.com/GatheusMana/Brasil-Sobre-Rodas)
