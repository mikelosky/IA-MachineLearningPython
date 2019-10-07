from heapq import heappush, heappop


def cost_uni(start, goal, graph):
    pr_queue = []
    print(pr_queue)

    heappush(pr_queue, (0, " ", start))  # implementazione un albero in cui i nodi genitori hanno un valore inveriore
    print(pr_queue)
    visited = set()
    while pr_queue:
        cost, path, current = heappop(pr_queue)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour, walk in graph[current]:
            heappush(pr_queue, (cost + walk, path + direction, neighbour))
            # print(pr_queue)
    return None


def getAjacentSpace(lab, rig, col):
    M = rig
    N = col
    graph = {(i, j): [] for i, r in enumerate(lab) for j, c in enumerate(r)}
    for i in range(0, M):
        for j in range(0, N):
            if lab[i][j] != "o":
                if i + 1 < M:
                    graph[(i, j)].append(("Down ", (i + 1, j), 3))
                if i - 1 >= 0:
                    graph[(i, j)].append(("Up ", (i - 1, j), 1))
                if j + 1 < N:
                    graph[(i, j)].append(("Dx ", (i, j + 1), 2))
                if j - 1 >= 0:
                    graph[(i, j)].append(("Sx ", (i, j - 1), 2))
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
                    return tuple([i, j])
    return None

def find_goal(lab):
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if lab[i][j] == 'g':
                return tuple([i, j])
    return None

if __name__ == "__main__":
    #Leggo il labirinto da file
    lab = read_fromfile()
    start = find_start(lab)
    goal = find_goal(lab)
    rig = len(lab)
    col = len(lab[0])
    graph = getAjacentSpace(lab, rig, col)
    percorso = cost_uni(start, goal, graph)

    if percorso == None:
        print("Nessun percorso valido")
    else:
        print(percorso)