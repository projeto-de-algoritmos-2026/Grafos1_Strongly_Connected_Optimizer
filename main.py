from node import *
from dfs_visit import DFS_visit
from bfs import BFS
import graph_ops as ops
import vals as dbg

def main():

    # O ARQUIVO DE ENTRADA DEVE ESTAR NO FORMATO
    # NOME1 X Y
    # NOME2 X Y
    # NOME1 NOME2
    #
    # E.G
    # A1 0.0 0.0
    # A2 5.0 -5.0
    # A3 -5.0 -5.0
    # A1 A2
    # A2 A3
    # A3 A1
    #
    # GRAFO RESULTANTE:
    #
    #
    #    />A1
    #   /    \
    #  /      \v
    # A3<------A2
    #
    # É POSSIVEL USAR COMENTÁRIOS COM #

    g = []

    with open("in.txt", "r") as file:
        for line in file:
            line = line.strip()

            if(line[0] == "#"):#Comentários
                continue  

            args = line.split(" ")
            if(len(args) == 3): # declarando Nó
                if(Node.find_node_by_name(g, args[0]) != -1):
                    raise ValueError(f"{line}\nTentando criar nó duplicado")

                g.append(Node(args[0], float(args[1]), float(args[2])))
            elif(len(args) == 2): # criando arestas
                ind1 = Node.find_node_by_name(g, args[0])
                ind2 = Node.find_node_by_name(g, args[1])
                
                if(ind1 == -1):
                    raise ValueError(f"{line}\nO primeiro nó na declaração de aresta não foi encontrado")
                if(ind2 == -1):
                    raise ValueError(f"{line}\nO segundo nó na declaração de aresta não foi encontrado")

                g[ind1].connect(g[ind2])

    if(dbg.debug):
        print("Grafo:")
        ops.print_graph(g)
        print("-=-=-=-=-=-=-")
    
    
    sccs = []   # Conjunto de SCC's
    # identifica os SCCS
    while(g):
        gi = ops.inverted(g)    # grafo inverso

        sni = DFS_visit(gi)     # encontra um sink node
        sn = g[Node.find_node(g, sni)]

        if(dbg.debug and dbg.rich):
            print(f"{sn.name} está em componente sink")
            print("-=-=-=-=-=-=-")
        
        bfg = BFS(g, sn)        # BFS a partir do sink node
        bfgi = BFS(gi, sni)     # BFS no grafo inverso
        scc = ops.intersect(bfg, bfgi) # encontra o SCC
        sccs.append(scc)
        g = ops.minus(g, scc)   # Subtrai o Scc do grafo
    
    if(dbg.debug):
        cont = 1
        for i in sccs:
            print(f"SCC {cont}:")
            ops.print_graph(i)
            print("-=-=-=-=-=-=-")
            cont += 1

    


if __name__ == "__main__":
    main()
