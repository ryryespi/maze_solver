# maze_solver
**Overview:**  In this project, you will be creating code to find a path through a maze, if such a path exists.

**Goal:**  To gain experience building path finding algorithms.

**Requirements:**  You are going to be given a set of mazes in text files to navigate.  Some of the mazes will be navigable and others will have no path available from the start point to the finish point.  The start and end can be at arbitrary positions in the maze, so you will have to read the maze file to find out where they are.  Mazes will vary in size, but will be surrounded on the outside by a set of walls and look something like the following:

<pre><code>
********************

*s.................*

*****.***********.**

*.***.*............*

*.***.***.***.****.*

*.........*...**...*

***.*****...****.***

*e...*****.......***

*********************
</code></pre>

The legend for the maze files is as follows:

* s  <- the starting position

*  e  <- the end goal for finishing the maze

*  walls <– you can’t walk through / occupy these spaces – maze will be surrounded by walls

*  .   <- empty space – you can occupy these spaces en route to the end

The only moves allowed in the maze are up, down, left and right.  Diagonal moves are disallowed.

In Python 3.x, write a program that will navigate from the starting point to the ending point of a maze.  An obvious choice would be an exhaustive search algorithm, but you have many options to consider, including algorithms not yet covered in class or not covered in the textbook.

Your code should output the route that it finds through the maze as well as the length of that route.  In addition, your code should be able to track 1) how long in seconds or milliseconds it takes to find a solution to a particular maze, and 2) how many basic operations are performed – you will need to include a README file or a block of comments at the top of your code explaining what you are counting as the basic operation.

The files will be stored in a folder called “mazes”, which you can assume will be placed in the same location as your source code, and each maze file will be named maze1.txt, maze2.txt, etc.  You’ve been provided with a number of sample mazes to practice on, but you should make sure to create your own for testing purposes.  

**by Ryan Espinosa**
