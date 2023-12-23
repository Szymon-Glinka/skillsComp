import logging

def fixMaze(mazeTofix):
    mazeFixedPlaceholder = ""
    mazeFixed = []
    mazeFinal = []
    iteration = 0
    insertedExit = False

    for line in mazeTofix: #itterate through each line in the maze
        mazeFixedPlaceholder = ""

        #================ check top and bottom of the maze ================
        if line == mazeTofix[0] or line == mazeTofix[-1]:
            for hash in line: #itterate through each character in top or bottom of maze
                if hash == ' ': #if character is a space, replace with E
                    mazeFixedPlaceholder += "E"
                    insertedExit = True
                else: #else, keep the character
                    mazeFixedPlaceholder += hash
        
            mazeFixed.append(mazeFixedPlaceholder) #append the fixed line to the mazeFixed list
        
        #================ check left and right of the maze ================
        else:
            lenOfline = len(line) #get length of the line

            for hash in line: #itterate through each character in the line
                if iteration == 0 and line[0] == " " or iteration == lenOfline-1 and line[-1] == " ": #if character is a space and is the first or last character in the line, replace with E
                    mazeFixedPlaceholder += "E"
                    insertedExit = True
                else: #else, keep the character
                    mazeFixedPlaceholder += hash
                iteration += 1

            mazeFixed.append(mazeFixedPlaceholder) #append the fixed line to the mazeFixed list
            iteration = 0

    #================ separate each character in each line ================
    for line in mazeFixed:
        mazeFinal.append(list(line))

    #================ return fixed maze or error message ================
    if insertedExit == False:
        return "NE"
    else:
        return mazeFinal
    
def solveMaze(mazeMain, start, visitedList):
    #set start coordinates
    row = start[0]
    col = start[1]

    #set size of maze
    maxRow = len(mazeMain)-1
    maxCol = len(mazeMain[0])-1 

    #declaring variables
    freeToGo = []
    repeat = True
    done1 = True
    done2 = True
    done3 = True
    done4 = True

    #================ Main loop solving maze ================ 
    while repeat: #while repeat is true, keep looping
        for i in range(4): #itterate through each direction
            #if dfs returns "E", return "Maze solved!"
            if dfs(mazeMain, row, col-1, maxRow, maxCol, visitedList) == "E" or dfs(mazeMain, row, col+1, maxRow, maxCol, visitedList) == "E" or dfs(mazeMain, row-1, col, maxRow, maxCol, visitedList) == "E" or dfs(mazeMain, row+1, col, maxRow, maxCol, visitedList) == "E":
                repeat = False
                return "MS"
            
            elif dfs(mazeMain, row+1, col, maxRow, maxCol, visitedList) and done1: #if dfs returns true, add the coordinates to the freeToGo list
                if visitedList[row+1][col] != "V": #if the coordinates are not already in the visitedList, add them to the freeToGo list
                    freeToGo.append([row+1, col])
                done1 = False

            elif dfs(mazeMain, row, col+1, maxRow, maxCol, visitedList) and done2: #if dfs returns true, add the coordinates to the freeToGo list
                if visitedList[row][col+1] != "V": #if the coordinates are not already in the visitedList, add them to the freeToGo list
                    freeToGo.append([row, col+1])
                done2 = False
        
            elif dfs(mazeMain, row-1, col, maxRow, maxCol, visitedList) and done3: #if dfs returns true, add the coordinates to the freeToGo list
                if visitedList[row-1][col] != "V": #if the coordinates are not already in the visitedList, add them to the freeToGo list
                    freeToGo.append([row-1, col])
                done3 = False

            elif dfs(mazeMain, row, col-1, maxRow, maxCol, visitedList) and done4: #if dfs returns true, add the coordinates to the freeToGo list
                if visitedList[row][col-1] != "V": #if the coordinates are not already in the visitedList, add them to the freeToGo list
                    freeToGo.append([row, col-1])
                done4 = False
        
        logging.debug(f"free to go: {freeToGo}")
        logging.debug(f"visited list in solve: {visitedList}")

        #resetting variables
        done1 = True
        done2 = True
        done3 = True
        done4 = True

        if len(freeToGo) == 0: #if there are no more freeToGo coordinates, return "No solution found."
            logging.debug(f"len of freeToGo == 0")
            return "NS"
        else:
            nextMove = freeToGo[-1] #set nextMove to the last item in the freeToGo list
            rowVcounter = 0 #reset rowVcounter
            for rowInVisited in visitedList: #itterate through each row in visitedList
                if rowVcounter == row: #if rowVcounter is equal to row, insert "V" in the nextMove column
                    rowInVisited[col] = "V"
                rowVcounter += 1

            #set row and col as next position
            row = nextMove[0] 
            col = nextMove[1]

            freeToGo.remove(nextMove) #remove nextMove from freeToGo

def dfs(mazeDFS, row, col, maxRow, maxCol, visitedMatrix):
    if row == 0 or row >= maxRow or col == 0 or col >= maxCol: #if row or col is out of bounds, return False
        if mazeDFS[row][col] == "E": #if row and col is equal to "E", return "E"
            return "E"
        return False
    
    elif mazeDFS[row][col] == "#": #if row and col is equal to "#", return False
        return False

    elif mazeDFS[row][col] == " ": #if row and col is equal to " ", return True
        return True
    
    elif visitedMatrix == "V": #if row and col is equal to "V", return False
        return False
    
def findStart(matrix, letter):
    for i, rowF in enumerate(matrix):
        for j, char in enumerate(rowF):
            if char == letter:
                return (i, j)
    return None

def checkIfMoreThanOneStart(matrixCheck):
    counts = {}
    for rowC in matrixCheck:
        for letter in rowC:
            if letter != "#" and letter != " " and letter != "E":
                if letter in counts:
                    counts[letter] += 1
                else:
                    counts[letter] = 1
                if counts[letter] > 1:
                    return True
    return False
    
def main(matrix):
    #================ check if maze is valid ================
    if len(matrix) == 1 and len(matrix[0]) == 1 and matrix[0] == "r": #if the maze is only one character and is "r", return True
        return True
    elif len(matrix) == 1 and len(matrix[0]) == 1 and matrix[0] != "r": #if the maze is only one character and is not "r", return False
        logging.debug(f"F1")
        return False

    #================ solve the actual maze================
    if fixMaze(matrix) == "NE":
        logging.debug(f"F2")
        return False
    else:
        fixedMaze = fixMaze(matrix) #convert maze to a format accepted by the solveMaze function
        logging.debug(f"fixedMaze: {fixedMaze}")

        start = findStart(fixedMaze, "r") #find the starting position of the maze
        logging.debug(f"Start: {start}")

        if checkIfMoreThanOneStart(matrix): #if there is more than one starting position, return False
            logging.debug(f"F3")
            return False

        #create a visited list
        height = len(fixedMaze)
        length = len(fixedMaze[0])
        visited = [[0 for _ in range(length)] for _ in range(height)]
        logging.debug(f"visited list: {visited}")
        
        #solve the maze
        conclusion = solveMaze(fixedMaze, start, visited)
        if conclusion == "MS":
            return True
        elif conclusion == "NS":
            logging.debug(f"F4")
            return False
    
if __name__ == '__main__':
    #logging setup
    logging.basicConfig(level=logging.ERROR, format="%(asctime)s %(levelname)s %(message)s", datefmt="%y-%m-%d %H:%M")

    maze = ["##############################",
            "### #     ## ##   #  ##   #  #",
            "# ### ##### ######### ########",
            "#    ##  #    ##             #",
            "# ######### ######### ##### ##",
            "##    ####  ##  ## #    ##  ##",
            "# ####### ##### # #####   # ##",
            "##   #    # #    #       #   #",
            "##### ######### ####### ### ##",
            "# #  #   # #          # #    #",
            "# ####### ########### # ### ##",
            "##                      #   ##",
            "  #######r################# ##",
            "# ##    ##    #   ## ###     #",
            "# ### ### # ##### ###### #####",
            "#     # ## # #  ##       # # #",
            "# # ##### ### ### ### # ### ##",
            "##            ##      ##  ## #",
            "# ####### ### ####### ### # ##",
            "# #   # # #           ###    #",
            "# ### ### ##### # ### # ### ##",
            "##   ###   #    # #        ###",
            "############# ##### ##### ####",
            "#####      #   #  # #  ###   #",
            "### # # ##### # ##############",
             "####          ##         # # #",
            "# ##### ######### ##### ######",
            "# #   #  #   #   #     #  # ##",
            "# ##### # # ##### ######### ##",
            "##############################"]

    print(main(maze))