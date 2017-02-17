import math

#filename = input("Enter filename (maze1.txt,maze2.txt,...,maze8.txt): ")
filename = "maze1.txt"

#read maze into file and save the row width
maze = []
k = 0
with open(filename,'r') as fp:
    colWidth = fp.readline().__len__()-1
with open(filename,'r') as fp:
    for line in fp:
        for ch in line:
            if ch != "\n":
                maze.append(ch)
                if ch == 's':
                    start = k
                if ch == 'e':
                    end = k
                k+=1


def printMaze():
    for i in range(0,maze.__len__()):
        print(maze[i], end="")
        if (i+1)%colWidth==0:
            print("\n", end="")
    print("\n")

def iup(index):
    if index-colWidth < 0:
        return -1
    return index-colWidth
def idwn(index):
    if index+colWidth > maze.__len__():
        return -1
    return index+colWidth
def ileft(index):
    if index%colWidth == 0:
        return -1
    return index - 1
def iright(index):
    if index%colWidth == colWidth-1:
        return -1
    return index + 1
def getXY(index):
    coord = []
    coord.append(index % colWidth)
    coord.append(math.floor(index / colWidth))

    return coord
def getDistance(num1, num2):
    n1 = getXY(num1)
    n2 = getXY(num2)
    return math.sqrt(math.pow((n1[0]-n2[0]),2)+math.pow((n1[1]-n2[1]),2))

printMaze()