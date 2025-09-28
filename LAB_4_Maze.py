# Names: Mishka Mansukhani; Akintunde Udo
# Date: September 16, 2026
# Description:

import check_input

def read_maze():
    '''description'''

    file_obj = open("maze.txt")
    maze_design = [] #hold the 2D maze: a list of rows, where each row is a list of chars

    for line in file_obj:  # read line by line
        spaces = [] # temporary list for this row
        for ch in line.rstrip("\n"):  # keep spaces, drop newline
            spaces.append(ch) # add each character as a separate element
        maze_design.append(spaces) # append the completed row to maze_design

    return maze_design # return the filled 2D list

def find_start(maze):
    ''' description '''

    # Loop through each row
    for r in range(len(maze)):
        # Loop through each column in that row
        for c in range(len(maze[r])):
            if maze[r][c] == "s":  # found the start
                return [r, c]
    # If no start found (shouldn’t happen if maze is valid)
    return [-1, -1]

def display_maze(maze, loc):
    '''description'''

    for r in range(len(maze)):# row index
        for c in range(len(maze[r])):# column index
            if [r, c] == loc: # if cell equals player location
                print("X", end="") # print without new line
            else:
                print(maze[r][c], end="") # print the maze's actual character
        print() # newline at the end of each row

def main():
    # s1: Load the maze into a 2D list
    maze = read_maze()

    # s2: Find the starting location
    loc = find_start(maze)

    print(" - Maze Game - ")

    # s3: Loop until the user finds the finish
    while True:
        # Display the maze with player's current location
        display_maze(maze, loc)

        # Menu of movement options
        print("\nChoose a direction:")
        print("1. North")
        print("2. South")
        print("3. West")
        print("4. East")

        # get user choice (validated by check_input)
        choice = check_input.get_int_range("Enter choice (1-4): ", 1, 4)

        # store the new location (start with current location)
        new_loc = loc.copy()

        # update based on movement choice
        if choice == 1:  # north
            new_loc[0] -= 1
        elif choice == 2:  # south
            new_loc[0] += 1
        elif choice == 3:  # west
            new_loc[1] -= 1
        elif choice == 4:  # east
            new_loc[1] += 1

            # check if move is valid (not into an asterisk)
        r, c = new_loc
        if maze[r][c] == "*":
            print("\nYou can't move here!\n")
        else:
            loc = new_loc  # update player’s location

        # check win condition
        if maze[loc[0]][loc[1]] == "f":
            display_maze(maze, loc)
            print("Congratulations! You solved the maze!")
            break

main()

"""if choice == 1:       # north
    new_loc[0] -= 1
    r, c = new_loc
    if maze[r][c] == "*":
        print("\nYou can't move here!\n")
    else:
        loc = new_loc
        if maze[loc[0]][loc[1]] == "f":
            display_maze(maze, loc)
            print("Congratulations! You solved the maze!")
            break
            
    if choice == 2:       # south
    new_loc[0] += 1
    r, c = new_loc
    if maze[r][c] == "*":
        print("\nYou can't move here!\n")
    else:
        loc = new_loc
        if maze[loc[0]][loc[1]] == "f":
            display_maze(maze, loc)
            print("Congratulations! You solved the maze!")
            break
            
    if choice == 3:       # west
    new_loc[0] -= 1
    r, c = new_loc
    if maze[r][c] == "*":
        print("\nYou can't move here!\n")
    else:
        loc = new_loc
        if maze[loc[0]][loc[1]] == "f":
            display_maze(maze, loc)
            print("Congratulations! You solved the maze!")
            break
            
    if choice == 4:       # east
    new_loc[0] += 1
    r, c = new_loc
    if maze[r][c] == "*":
        print("\nYou can't move here!\n")
    else:
        loc = new_loc
        if maze[loc[0]][loc[1]] == "f":
            display_maze(maze, loc)
            print("Congratulations! You solved the maze!")
            break"""




