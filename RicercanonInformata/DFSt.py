import collections

def D_F_S(start, goal, graph):
    visited = set()
    stack = collections.deque([start])
    path = start
    while stack:
        current = stack.pop()
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for vicini in graph[current]:
            stack.append((path , vicini))
    return None

def createListAdjancet(lab , rig, col):
    M = rig
    N = col
    graph = list()
    for i in range(0, M):
        for j in range(0, N):
            if lab[i][j] != "o":
                if i + 1 < M and lab[i + 1][j] != "o":
                    graph[(i, j)].append((i + 1, j))
                if i - 1 >= 0 and lab[i - 1][j] != "o":
                    graph[(i, j)].append((i - 1, j))
                if j + 1 < N and lab[i][j + 1] != "o":
                    graph[(i, j)].append((i, j + 1))
                if j - 1 >= 0 and lab[i][j - 1] != "o":
                    graph[(i, j)].append((i, j - 1))
    return graph

def read_fromfile():
    lab = list()

    with open("C:/Users/MkPc/Desktop/python-bfs-master/python-bfs-master/maze1.txt") as file:
        for line in file:
            lab.append(list(line.rstrip()))
    return lab

def find_start(lab):
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if lab[i][j] == 's':
                    return tuple([ i, j])
    return None

def find_goal(lab):
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if lab[i][j] == 'g':
                return tuple([ i, j])
    return None

if __name__ == "__main__":
    #Leggo il labirinto da file
    lab = read_fromfile()
    start = find_start(lab)
    goal = find_goal(lab)
    rig = len(lab)
    col = len(lab[0])
    graph = createListAdjancet(lab, rig, col)
    percorso = D_F_S(start, goal , graph)

    if percorso == None:
        print("Nessun percorso valido")
    else:
        print(percorso)