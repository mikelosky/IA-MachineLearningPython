import random
import numpy

def writeFile(file2,sizex,sizey,n_ost,startx,starty,goalx,goaly):
    lines = list()
    lab = list()
    mat = [[0 for x in range(sizey + 1)] for y in range(sizex + 1)]
    for i in range(sizex + 1):
        for j in range(sizey + 1):
            if i == sizex  or i == 0 or j == sizey  or j == 0:
                mat[i][j] = "o"
            else:
                mat[i][j] = "."
    mat[startx][starty] = 's'
    mat[goalx][goaly] = 'g'

    while(n_ost > 0):
        randomx = random.randrange(1, sizex - 1, 1)
        randomy = random.randrange(1, sizey - 1, 1)
        if mat[randomx][randomy]!='o' and mat[randomx][randomy]!='s' and mat[randomx][randomy]!='g':
            mat[randomx][randomy]='o'
            n_ost -= 1

    for i in range(sizex + 1):
        for j in range(sizey + 1):
            lines.append(mat[i][j])
            s = "".join(lines)

        file2.write(s + "\n")
        lines.clear()


if __name__ == "__main__":
    file2 = open(r"mazetest.txt", "w+")
    startx = 1
    starty = 1
    goalx = 8
    goaly = 15
    sizey = 20
    sizex = 9
    n_ost = 30
    writeFile(file2,sizex,sizey,n_ost,startx,starty,goalx,goaly)