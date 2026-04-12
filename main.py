from node import *
from dfs_visit import DFS_visit

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
