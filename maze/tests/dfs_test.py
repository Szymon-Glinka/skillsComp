#TO DO: make program find maxCol and maxRow and row and col

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
            
        #resetting variables
        done1 = True
        done2 = True
        done3 = True
        done4 = True

        print(freeToGo)
        print(visitedList)

        if len(freeToGo) == 0: #if there are no more freeToGo coordinates, return "No solution found."
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
    
    






if __name__ == '__main__':
    maze = [['#', '#', '#', '#', '#', '#', '#', '#'], ['#', ' ', '#', 'r', '#', '#', '#', '#'], ['#', ' ', '#', ' ', '#', ' ', ' ', 'E'], ['#', ' ', '#', ' ', '#', ' ', '#', '#'], ['#', ' ', '#', ' ', '#', ' ', '#', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', '#', '#', '#', '#', '#', '#']]

    visited = [
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
    ]

   


    start = (1, 3)
    print(solveMaze(maze, start, visited))