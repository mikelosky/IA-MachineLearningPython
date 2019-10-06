import random

def writeFile(file,sizex,sizey,n_ost):
    lines = list()
    lab = list()
    for i in range(sizex + 1):
        for j in range(sizey + 1):
            if i == sizex  or i == 0 or j == sizey  or j == 0:
                lines.append('*')
            else:
                if random.uniform(0 , 1) > 0.7 and n_ost > 0:
                    lines.append('o')
                    n_ost-=1
                else:
                    lines.append(' ')
        file.write("%s\n" % lines)
        lines.clear()
    with file as file1:
        for line in file1:
            lab.append(list(line.rstrip()))
    #TODO: Implementare la verifica del copleto inseriemnto dei Walls
    while(n_ost > 0):
        for i in range(sizex + 1):
            for j in range(sizey + 1):
                if random.uniform(0 , 1) > 0.7 and lab[i][j] != '*':
                    line.append('o')
                    n_ost - 1







if __name__ == "__main__":
    file = open(r"maze.txt","w+")
    sizex = 5
    sizey = 5
    n_ost = 2
    writeFile(file,sizex,sizey,n_ost)