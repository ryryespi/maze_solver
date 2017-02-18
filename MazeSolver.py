import math
import datetime

filename = input("Enter filename (maze1.txt,maze2.txt,...,maze8.txt): \n")
startingTime = datetime.datetime.now()

#read maze into file and save the row width=====================
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

#functions=============================================

def printMaze():
    for i in range(0,maze.__len__()):
        print(maze[i], end="")
        if (i+1)%colWidth==0:
            print("\n", end="")
    print("\n", end="")

print("ORIGINAL MAZE")
printMaze()

c = {'p', '*'}
def iup(index):

    if index-colWidth < 0 or (maze[index - colWidth] in c):
        return -1
    return index-colWidth

def idwn(index):
    if index+colWidth > maze.__len__()-1 or (maze[index + colWidth] in c):
        return -1
    return index+colWidth

def ileft(index):
    if index%colWidth == 0 or (maze[index - 1] in c):
        return -1
    return index - 1

def iright(index):
    if index%colWidth == colWidth-1 or (maze[index + 1] in c):
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

#clean up maze dead ends
deadEnd = True
while deadEnd == True:
    deadEnd = False
    for i in range(0, maze.__len__()):
        paths = 0
        if maze[i] =='.':
            if iup(i) == -1:
                paths +=1
            if idwn(i) == -1:
                paths +=1
            if ileft(i) == -1:
                paths +=1
            if iright(i) == -1:
                paths +=1
            if paths == 3:
                maze[i]='*'
                deadEnd = True

#A* solution
step = 0
sol = []
sol.append(start)
while sol[step] != end:
    nextStep = sol[step]
    cmpList = []
    if iright(nextStep) != -1 and maze[iright(nextStep)] != 's':
        cmpList.append(iright(nextStep))

    if idwn(nextStep) != -1 and maze[idwn(nextStep)] != 's':
        cmpList.append(idwn(nextStep))

    if ileft(nextStep) != -1 and maze[ileft(nextStep)] != 's':
        cmpList.append(ileft(nextStep))

    if iup(nextStep) != -1 and maze[iup(nextStep)] != 's':
        cmpList.append(iup(nextStep))

    if cmpList.__len__():
        least = getDistance(cmpList[0],end)
        nextStep = cmpList[0]
        for index in cmpList:
            if least > getDistance(index,end):
                nextStep = index
    else:
        nextStep = sol[step]
    if nextStep == start:
        break

    if nextStep == sol[step]:
        maze[nextStep]='*'
        sol.pop()
        step-=1
    else:
        sol.append(nextStep)
        if maze[nextStep]!= 'e':
            maze[nextStep] ='p'
        step += 1

endingTime = datetime.datetime.now()


print("SOLVED MAZE")
printMaze()
print("Maze solved in ", endingTime-startingTime," milliseconds \n")

if start == sol.pop():
    print("The maze is unsolvable")

if input("list all elements in solution?[y,n]: ").lower() == 'y':
    for i in range(0,sol.__len__()):
        coord = getXY(sol[i])
        print("[",coord[0],",",coord[1],"]")


