import copy
import collections


def DFS_prof_lim(start, goal, graph, depth):
    visited = set()
    stack = collections.deque([("", start)])
    temp_depth = copy.deepcopy(depth)
    risp = ""
    while stack:
        path, current = stack.pop()
        if temp_depth >= 0:
            temp_depth = temp_depth - 1
            if current == goal:
                return path
            if current in visited:
                continue
            visited.add(current)
            for direzione, vicini in graph[current]:
                stack.append((path + direzione, vicini))
        else:
            print("profondità max raggiunta. ")

    return None


def createListAdjancet(lab, rig, col):
    M = rig
    N = col
    graph = {(i, j): [] for i, r in enumerate(lab) for j, c in enumerate(r)}
    for i in range(0, M):
        for j in range(0, N):
            if lab[i][j] != "o":
                if i + 1 < M:
                    graph[(i, j)].append(("Down ", (i + 1, j)))
                if i - 1 >= 0:
                    graph[(i, j)].append(("Up ", (i - 1, j)))
                if j + 1 < N:
                    graph[(i, j)].append(("Dx ", (i, j + 1)))
                if j - 1 >= 0:
                    graph[(i, j)].append(("Sx ", (i, j - 1)))
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
    # Leggo il labirinto da file
    lab = read_fromfile()
    start = find_start(lab)
    goal = find_goal(lab)
    depth = 1000
    rig = len(lab)
    col = len(lab[0])
    graph = createListAdjancet(lab, rig, col)
    percorso = DFS_prof_lim(start, goal, graph, depth)

    if percorso == None:
        print("Nessun percorso valido")
    else:
        print(percorso)
