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
            


class DFS_Data:
    def __init__(self):
        self.visited = set()
        self.last = Node("Vazio", 0, 0)

# Devolve um nó em componente source
def DFS_visit(*g: Node) -> Node:
    data = DFS_Data()
    next = 0
    while(next != -1):
        _DFS_visit(g[next], data)
        next = first_unvisited(g, data)

    return data.last

def _DFS_visit(n, data: DFS_Data):
    data.visited.add(n)
    for v in n.neighbors:
        if(v not in data.visited):
            _DFS_visit(v, data)
    data.last = n
    
        


def first_unvisited(g: list[Node], data: DFS_Data) -> int:
    for i in range(0, len(g)):
        if(g[i] not in data.visited):
            return i
    return -1


def main():
    a1 = Node("A1", 0, 0)
    a2 = Node("A2", 0, 0)
    a3 = Node("A3", 0, 0)
    b1 = Node("B1", 0, 0)
    b2 = Node("B2", 0, 0)
    b3 = Node("B3", 0, 0)
    c1 = Node("C1", 0, 0)
    c2 = Node("C2", 0, 0)
    c3 = Node("C3", 0, 0)

    a1.connect(a2)
    a2.connect(a3)
    a3.connect(a1)

    b1.connect(b2)
    b2.connect(b3, c3)
    b3.connect(b1, a2)

    c1.connect(c2)
    c2.connect(c3)
    c3.connect(c1)

    print(DFS_visit(a1,a2,a3,b1,b2,b3,c1,c2,c3).name)



if __name__ == "__main__":
    main()