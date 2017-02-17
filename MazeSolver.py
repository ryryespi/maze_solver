

filename = input("Enter filename (maze1.txt,maze2.txt,...,maze8.txt): ")
print(filename)

#read maze into file and save the row width
maze = []
with open(filename,'r') as fp:
    colWidth = fp.readline().__len__()
with open(filename,'r') as fp:
    for line in fp:
        for ch in line:
            maze.append(ch)


def printMaze():
    for i in range(0,maze.__len__()):
        print(maze[i], end="")
        if(i+1%colWidth==0):
            print("\n")

printMaze()