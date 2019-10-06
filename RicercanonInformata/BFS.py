import os

#leggiamo il file dove abbiamo implementato il nostro labirinto

def B_F_S(lab, start, goal):
    coda = [start]
    visitati = set()

    while len(coda) != 0:
        if coda[0] == start:
            perc = [coda.pop(0)]
        else:
            perc = coda.pop(0)
        front = perc[-1]
        if front == goal:
            return perc
        elif front not in visitati:
            for vicinanze in prendiVicinanze(front,lab,visitati):
                newPerc = list(perc)
                newPerc.append(vicinanze)
                coda.append(newPerc)

            visitati.add(front)
    return None


def prendiVicinanze(front,lab,visitati):
    fronts = list()

    fronts.append((front[0] - 1, front[1]))
    fronts.append((front[0] + 1, front[1]))
    fronts.append((front[0], front[1] - 1))
    fronts.append((front[0], front[1] + 1))
    final = list()
    for i in fronts:
        if lab[i[0]][i[1]] != 'o' and i not in visitati:
            final.append(i)
    return final

def read_fromfile():
    lab = list()

    with open("C:/Users/MkPc/Desktop/python-bfs-master/python-bfs-master/maze1.txt") as file:
        for line in file:
            lab.append(list(line.rstrip()))
    return lab

#troviamo il nostro start point e end point

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

    percorso = B_F_S(lab, start, goal)

    if percorso == None:
        print("Nessun percorso valido")
    else:
        print(percorso)

