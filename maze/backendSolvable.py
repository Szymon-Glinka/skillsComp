import logging
import copy


def fixMaze(mazeTofix):
    """Finds and places exits wherever possible in the maze, prepers maze for solveMaze function
    If maze is impossible to solve - there is no exit, returns 'NE'(no exit).
    Takes in a matrix as an argument, returns a fixed matrix or 'NE'"""

    #--- declaring variables ---
    mazeFixedPlaceholder = ""
    mazeFixed = []
    mazeFinal = []
    iteration = 0
    insertedExit = False

    for line in mazeTofix: #itterate through each line in the maze
        mazeFixedPlaceholder = ""

        #--- check top and bottom of the maze ---
        if line == mazeTofix[0] or line == mazeTofix[-1]:
            #--- tterate through each character in top or bottom of maze ---
            for hash in line: 
                #---  #if character is a space, replace with E ---
                if hash == ' ':
                    mazeFixedPlaceholder += "E"
                    insertedExit = True
                else:
                    mazeFixedPlaceholder += hash
        
            mazeFixed.append(mazeFixedPlaceholder) #append the fixed line to the mazeFixed list
        
        #--- check left and right of the maze ---
        else:
            lenOfline = len(line) #get length of the line

            #--- itterate through each character in the line ---
            for hash in line: 
                #--- if character is a space and is the first or last character in the line, replace with E ---
                if iteration == 0 and line[0] == " " or iteration == lenOfline-1 and line[-1] == " ": 
                    mazeFixedPlaceholder += "E"
                    insertedExit = True
                else:
                    mazeFixedPlaceholder += hash
                iteration += 1

            mazeFixed.append(mazeFixedPlaceholder) #append the fixed line to the mazeFixed list
            iteration = 0

    #--- separate each character in each line ---
    for line in mazeFixed:
        mazeFinal.append(list(line))

    #--- return fixed maze or error message ---
    if insertedExit == False:
        return "NE"
    else:
        return mazeFinal
    

def dfs(mazeMain, start, visitedList):
    """Solves the maze using something similar to DFS.
    Takes in a matrix, start coordinates and a visitedList as arguments, returns 'MS' (maze solved) or 'NS' (no solution) and list of visited places"""

    #set start coordinates
    row = start[0]
    col = start[1]

    #set size of maze
    maxRow = len(mazeMain)-1
    maxCol = len(mazeMain[0])-1 
    
    #declaring variables
    rowEcounter = 0
    freeToGo = []
    repeat = True
    done1 = True
    done2 = True
    done3 = True
    done4 = True
    forkCounter = 0
    listOfVcopies = []

    #--- Main loop solving maze ---
    #while repeat is true, keep looping
    while repeat: 
        rowVcounter = 0 #reset rowVcounter
        forkCounter = 0 #reset forkCounter

        #--- Appending V (visited) to curent possition ---
        for rowInVisited in visitedList: 
            #--- if rowVcounter is equal to row, insert "V" in the nextMove column ---
            if rowVcounter == row: 
                rowInVisited[col] = "V"
            rowVcounter += 1

        for i in range(4): 
            #==== Look for exit ===
            #--- if exit is on the right append E to visited list and return true---
            if mazeMain[row+1][col] == "E":
                repeat = False

                #--- appending "E" to visited list ---
                for rowInVisited in visitedList: 
                    if rowEcounter == row+1: 
                        rowInVisited[col] = "E"
                    rowEcounter += 1

                return "MS", visitedList
            
            #--- if exit is on the bottom append E to visited list and return true---
            elif mazeMain[row][col+1] == "E":
                repeat = False

                #--- appending "E" to visited list ---
                for rowInVisited in visitedList: 
                    if rowEcounter == row: 
                        rowInVisited[col+1] = "E"
                    rowEcounter += 1

                return "MS", visitedList
            
            #--- if exit is on the left append E to visited list and return true---
            elif mazeMain[row-1][col] == "E":
                repeat = False
                
                #--- appending "E" to visited list ---
                for rowInVisited in visitedList: 
                    if rowEcounter == row-1: 
                        rowInVisited[col] = "E"
                    rowEcounter += 1

                return "MS", visitedList
            
            #--- if exit is on the top append E to visited list and return true---
            elif mazeMain[row][col-1] == "E":
                repeat = False
                
                #--- appending "E" to visited list ---
                for rowInVisited in visitedList: 
                    if rowEcounter == row: 
                        rowInVisited[col-1] = "E"
                    rowEcounter += 1

                return "MS", visitedList
            
            #==== Check for possible moves ====
            #--- if right is empty and not visited, append to freeToGo and increase forkCounter ---
            elif mazeMain[row+1][col] == " " and done1 and row+1 <= maxRow: 
                if visitedList[row+1][col] != "V": 
                    freeToGo.append([row+1, col])
                    forkCounter += 1
                done1 = False
                
            #--- if bottom is empty and not visited, append to freeToGo and increase forkCounter ---
            elif mazeMain[row][col+1] == " " and done2 and col+1 <= maxCol:
                if visitedList[row][col+1] != "V":
                    freeToGo.append([row, col+1])
                    forkCounter += 1
                done2 = False

            #--- if left is empty and not visited, append to freeToGo and increase forkCounter ---
            elif mazeMain[row-1][col] == " " and done3 and row-1 >= 0:
                if visitedList[row-1][col] != "V": 
                    freeToGo.append([row-1, col])
                    forkCounter += 1
                done3 = False

            #--- if top is empty and not visited, append to freeToGo and increase forkCounter ---
            elif mazeMain[row][col-1] == " " and done4 and col-1 >= 0:
                if visitedList[row][col-1] != "V":
                    freeToGo.append([row, col-1])
                    forkCounter += 1
                done4 = False

        #--- debiugging ---
        logging.debug(f"free to go: {freeToGo}")
        logging.debug(f"visited list in solve: {visitedList}")

        #--- resetting variables ---
        done1 = True
        done2 = True
        done3 = True
        done4 = True

        #==== Make next move ====
        #--- if there are no more freeToGo coordinates, return "No solution found." ---
        if len(freeToGo) == 0:
            logging.debug(f"len of freeToGo == 0") #debugging
            return "NS", None
        
        else:
            nextMove = freeToGo[-1] #set nextMove to the last item in the freeToGo list

            #--- set row and col as next position ---
            row = nextMove[0] 
            col = nextMove[1]

            freeToGo.remove(nextMove) #remove nextMove from freeToGo

        #--- if there is a fork append copy visited to listOfVcopies ---
        if forkCounter > 1:
            for i in range(forkCounter-1):
                copyOfVisited = copy.deepcopy(visitedList)
                listOfVcopies.append(copyOfVisited)
        #--- if there is a dead end, remove last item from listOfVcopies and set list of visited as the last item in listOfVcopies ---
        elif forkCounter == 0:
            visitedList = listOfVcopies[-1]
            listOfVcopies.remove(visitedList)
            



def findStart(matrix, letter):
    """Finds the starting position of the maze and checks if there is more than one startiung position.
    If there is, return false because maze can have only one starting position.
    Takes in a matrix and a letter to find as arguments, returns the coordinates of the letter, if there is one starting position.
    If there is more than one starting position, return 'MS{}'(multiple starting positions)"""

    #--- declaring variables ---
    counts = {}
    howManyStarts = ""
    pos = []

    #--- itterate through each row in the matrix to find starting position---
    for i, rowF in enumerate(matrix):
        for j, char in enumerate(rowF):
            if char == letter:
                pos.append(i)
                pos.append(j)

    #--- itterate through each row in the matrix to find number of starting positions---
    for rowC in matrix:
        for letter in rowC:
            #--- start checkling if there is more than one starting position, dont take into account walls, empy paths and exits---
            if letter != "#" and letter != " " and letter != "E":
                if letter in counts:
                    counts[letter] += 1
                else:
                    counts[letter] = 1
                if counts[letter] > 1:
                    howManyStarts = "MSP"
                
    if howManyStarts == "MSP":
        return howManyStarts
    else:
        return pos
    

def getMazeFromTXT(path):
    """Gets the maze from a text file and returns it as a matrix"""
    maze = [] 

    #--- open the maze.txt file and append each line to the maze list ---
    with open(path, "r") as file:
        for line in file:
            #--- remove all the unnecessary characters from the line ---
            line1 = line.strip()
            line2 = line1.replace("[","")
            line3 = line2.replace("]","")
            line4 = line3.replace(",","")
            line5 = line4.replace('"',"")
            line6 = line5.replace("'","")
            line7 = line6.replace("\n","")

            maze.append(line7) #append the line to the maze list

    return maze

def pathTranslate(path, startingLetter):
    """This function converts the path to exit to a list of moves that the robot can understand.
    It takes as input path to exit and starting letter coordinates, it returns a list of moves (RIGHT, LEFT, UP, DOWN)"""

    #==== declaring variables ====
    moves = []
    maxRow = len(path)-1 #get max row
    maxCol = len(path[0])-1 #get max column

    #--- set starting position ---
    row = startingLetter[0]
    col = startingLetter[1]

    repeat = True
    
    #--- main loop ---
    while repeat:
        check = True #set check to true

        #==== Check for exit ====
        #--- if exit is on the bottom append "DOWN" and return list of moves---
        if row < maxRow and path[row+1][col] == "E":
            moves.append("DOWN")

            #--- set repeat and check to false so the loop stops ---
            repeat = False
            check = False

            return moves
        
        #--- if exit is on the right append "RIGHT" and return list of moves---
        elif col < maxCol and path[row][col+1] == "E":
            moves.append("RIGHT")

            #--- set repeat and check to false so the loop stops ---
            repeat = False
            check = False

            return moves
        
        #--- if exit is on the top append "UP" and return list of moves---
        elif row > 0 and path[row-1][col] == "E":
            moves.append("UP")

            #--- set repeat and check to false so the loop stops ---
            repeat = False
            check = False

            return moves
        
        #--- if exit is on the left append "LEFT" and return list of moves---
        elif col > 0 and path[row][col-1] == "E":
            moves.append("LEFT")

            #--- set repeat and check to false so the loop stops ---
            repeat = False
            check = False

            return moves
        

        #=== Check for possible moves ===
        #--- if bottom is "V" (possible to go to) append "DOWN" and remove "V" from this position and set "check" to false so no other if statement is executed ---
        if row < maxRow and path[row+1][col] == "V" and check:
            moves.append("DOWN")

            #--- remove "V" from this position ---
            path[row].pop(col)
            path[row].insert(col, " ")

            row += 1
            check = False

        #--- if right is "V" (possible to go to) append "RIGHT" and remove "V" from this position and set "check" to false so no other if statement is executed ---
        elif col < maxCol and path[row][col+1] == "V" and check: 
            moves.append("RIGHT")

            #--- remove "V" from this position ---
            path[row].pop(col)
            path[row].insert(col, " ")

            col += 1
            check = False

        #--- if top is "V" (possible to go to) append "UP" and remove "V" from this position and set "check" to false so no other if statement is executed ---
        elif row > 0 and path[row-1][col] == "V" and check:
            moves.append("UP")

            #--- remove "V" from this position ---
            path[row].pop(col)
            path[row].insert(col, " ")

            row -= 1
            check = False

        #--- if left is "V" (possible to go to) append "LEFT" and remove "V" from this position and set "check" to false so no other if statement is executed --
        elif col > 0 and path[row][col-1] == "V" and check:
            moves.append("LEFT")

            #--- remove "V" from this position ---
            path[row].pop(col)
            path[row].insert(col, " ")

            col -= 1
            check = False