#function to find the exit of the maze
def putExit(mazeTofix):
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
        return "No exit found! Maze impossible to solve!"
    else:
        return mazeFinal
    
        
    
def dfs():
    pass

if __name__ == '__main__':
    maze = ["########",
        	  "# #r####",
        	  "# # #   ",
        	  "# # # ##",
        	  "# # # ##",
        	  "#      #",
        	  "########"]
    
    print(putExit(maze))