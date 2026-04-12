class Node:
    def __init__(self, name: str, x: float, y: float):
        self.name = name
        self.x = x # Posição em X
        self.y = y # Posição em Y
        self.neighbors = [] # arestas (vizinhos)


    # cria uma aresta entre esses nós e os nós em "lista_nós"
    # pode ser chamada com uma quantidade arbitraria de argumentos no.connect(no1, no2, no3)
    # ou com uma lista desempacotada: no.connect(*nos_para_conectar)
    def connect(self, *node: Node) -> None:
        for n in node:
            self.neighbors.append(n)


    # Imprime a lista de vizinhos por nome
    def print_vizinhos(self) -> None:
        print("[", end="")

        for i in range(0,len(self.neighbors)-1):
            print(self.neighbors[i].name, end=", ")

        print(self.neighbors[-1].name, end="")
        print("]")

if __name__ == "__main__":
    print("Rodando o arquivo node.py, você quis dizer main.py?")