import logging
from backendSolvable import fixMaze, dfs, findStart, getMazeFromTXT
    
def mazeSolver(matrix, startingLetter):
    """Solves a maze. Takes in matrix(maze) and startingLetter as arguments.
    Set startingLetter to whatever letter the maze uses to represent the starting position.
    This function returns True if the maze is solvable, False if it is not.
    Additionaly if maze is not solvable, it returns a string explaining why it is not solvable."""

    whyNotSolvable = "" #variable to store why the maze is not solvable

    #==== check if maze is valid ====
    #--- if the maze is only one character and is "r", return True. Otherwise return false ---
    if len(matrix) == 1 and len(matrix[0]) == 1 and matrix[0] == startingLetter:
        return True, None
    elif len(matrix) == 1 and len(matrix[0]) == 1 and matrix[0] != startingLetter:
        whyNotSolvable = f"E1 - Maze is only one character and it's not {startingLetter}"
        return False, whyNotSolvable

    #==== solve the actual maze ====
    #--- if there is no exit, return False. Else solve the maze ---
    if fixMaze(matrix) == "NE":
        whyNotSolvable = "E2 - No exit found"
        return False, whyNotSolvable
    else:
        fixedMaze = fixMaze(matrix) #convert maze to a format accepted by the solveMaze function
        exitCoord = findStart(matrix, startingLetter) #find the exit coordinates

        #--- if there is more than one starting position, return False, if no starting pos found return false, otherwise set start as exitCoord ---
        if exitCoord == "MSP":
            whyNotSolvable = "E3 - More than one starting position"
            return False, whyNotSolvable
        elif len(exitCoord) == 0:
            whyNotSolvable = f"E4 - starting position for letter {startingLetter} not found"
            return False, whyNotSolvable
        else:
            start = exitCoord

        #--- create an empty list of visited places ---
        height = len(fixedMaze)
        length = len(fixedMaze[0])
        visited = [[0 for _ in range(length)] for _ in range(height)]
        
        #==== solve the maze ====
        conclusion, visitedList = dfs(fixedMaze, start, visited)

        #--- if the conclusion is "MS", return True. Else return False ---
        if conclusion == "MS":
            return True, None
        elif conclusion == "NS":
            whyNotSolvable = "E5 - No solution found"
            return False, whyNotSolvable
           

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR, format="%(asctime)s %(levelname)s %(message)s", datefmt="%y-%m-%d %H:%M") #logging setup
    maze = getMazeFromTXT(r"F:\skillscomp\z1textFiles\labirynt9.txt") #get maze from txt file
    solvable, info = mazeSolver(maze, "r") #solve the maze
    print(solvable, info) #print the result
