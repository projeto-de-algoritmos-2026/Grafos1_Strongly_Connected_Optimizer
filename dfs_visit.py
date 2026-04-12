from node import *

# Dados adicionais necessários para DFS visit (hash de nós visitados e o último nó removido do stack)
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
        next = _DFS_first_unvisited(g, data)

    return data.last

# recursivo
def _DFS_visit(n, data: DFS_Data):
    data.visited.add(n)
    for v in n.neighbors:
        if(v not in data.visited):
            _DFS_visit(v, data)
    data.last = n
    
# retorna o índice do primeiro nó não visitado
def _DFS_first_unvisited(g: list[Node], data: DFS_Data) -> int:
    for i in range(0, len(g)):
        if(g[i] not in data.visited):
            return i
    return -1


if __name__ == "__main__":
    print("Rodando o arquivo dfs.py, você quis dizer main.py?")
