# Strongly Connected Optimizer (SCO)

Número da Lista: 37<br>
Conteúdo da Disciplina: Grafos 1<br>

## Apresentação

![Link Apresentação](https://youtu.be/YvB967L34Pg)

## Alunos

|Matrícula | Aluno |
| -- | -- |
| 21/1029512  |  Laís Cecília Soares Paes |
| 22/1008697  |  Sunamita Vitória Rodrigues dos Santos |

## Sobre 
O Strongly Connected Optimizer (SCO) é uma ferramenta desenvolvida para análise e otimização de conectividade em grafos direcionados. O projeto resolve um problema clássico de infraestrutura e logística: como tornar um sistema totalmente acessível com um baixo custo de deslocamento?

Identificação de SCCs: O programa utiliza uma abordagem baseada em buscas em profundidade (DFS) e largura (BFS) para isolar os Componentes Fortemente Conexos (SCCs) — "ilhas" onde todos os nós alcançam uns aos outros.

Otimização Geométrica: Utilizando as coordenadas cartesianas $(x, y)$ de cada nó, o algoritmo calcula a Distância Euclidiana entre todos os componentes isolados.

Sugestão de Arestas: O SCO identifica os pares de nós mais próximos entre componentes diferentes e sugere a criação de arestas (ida e volta) para unificar o grafo, garantindo que ele se torne um único componente fortemente conexo.

## Screenshots

### 1. Interface Inicial
A interface limpa pronta para receber o arquivo de entrada.
![Interface Inicial](./Images/interface_inicial.png)

### 2. Processamento e Logs
Exemplo do log detalhado identificando cada um dos SCCs e calculando as distâncias.

![Logs de Processamento](./Images/logs.png)

### 3. Projeto em Funcionamento (Grafo Final)
O resultado visual com as arestas originais e as sugestões de conexão em vermelho.
![Projeto Funcionando](./Images/projeto_funcionando2.png)

## Instalação 
Linguagem: Python<br>
Bibliotecas Necessárias: matplotlib, networkx, tkinter (nativa).
Certifique-se de ter o Python instalado. Em seguida, instale as dependências de visualização via terminal:

`pip install matplotlib networkx`

Comando para rodar:

`python gui.py`

## Uso 

Prepare o arquivo de entrada: Crie um arquivo .txt seguindo o formato:

Nós: NOME COORD_X COORD_Y (Ex: A 100 200)

Arestas: ORIGEM DESTINO (Ex: A B)

Carregue no Programa: Clique em "Carregar in.txt" e selecione seu arquivo.

Processe: Clique em "Processar Grafo".

Visualize: O painel esquerdo exibirá a análise lógica e os SCCs encontrados. O painel direito mostrará o grafo original e, logo abaixo, o grafo otimizado com as novas conexões destacadas em vermelho tracejado.

## Outros 

Complexidade Algorítmica:
Identificação de SCCs: $O(V + E)$, utilizando uma estratégia inspirada no algoritmo de Kosaraju.
Conectividade Total: $O(V^2)$ no pior caso para a busca exaustiva de distâncias mínimas entre componentes, garantindo a precisão geométrica das sugestões.
O projeto demonstra como conceitos abstratos de teoria de grafos podem ser aplicados em conjunto com geometria analítica para resolver problemas de conectividade em mapas e redes de comunicação.
