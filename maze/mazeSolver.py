import logging
from backendSolvable import fixMaze, dfs, findStart
    
def mazeSolver(matrix, startingLetter):
    """Solves a maze. Takes in matrix(maze) and startingLetter as arguments.
    Set startingLetter to whatever letter the maze uses to represent the starting position."""

    #==== check if maze is valid ====
    #--- if the maze is only one character and is "r", return True. Otherwise return false ---
    if len(matrix) == 1 and len(matrix[0]) == 1 and matrix[0] == startingLetter:
        return True
    elif len(matrix) == 1 and len(matrix[0]) == 1 and matrix[0] != startingLetter:
        logging.error(f"F1 - Maze is only one character and is not {startingLetter}")
        return False

    #==== solve the actual maze ====
    #--- if there is no exit, return False. Else solve the maze ---
    if fixMaze(matrix) == "NE":
        logging.error(f"F2 - No exit found")
        return False
    else:
        fixedMaze = fixMaze(matrix) #convert maze to a format accepted by the solveMaze function
        exitCoord = findStart(matrix, startingLetter) #find the exit coordinates

        #--- if there is more than one starting position, return False. Else set starting position ---
        if exitCoord == "MSP":
            logging.error(f"F3 - More than one starting position")
            return False
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
            return True
        elif conclusion == "NS":
            logging.error(f"F4 - No solution found")
            return False
           

if __name__ == '__main__':
    #logging setup
    logging.basicConfig(level=logging.ERROR, format="%(asctime)s %(levelname)s %(message)s", datefmt="%y-%m-%d %H:%M")

    maze = [' # #   #  ',
            '      ### ',
            '## #  ##  ',
            '   #####  ',
            ' # #####  ',
            '## ##r # #',
            '    # # # ',
            ' # # #  ##',
            ' ###  ####',
            '       # #']

    print(mazeSolver(maze, "r"))
