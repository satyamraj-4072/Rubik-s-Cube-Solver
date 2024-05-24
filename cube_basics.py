from random import randint, choice

class RubiksCube:
    """
    Class containing the rubiks struct code
    """

    def __init__(
        cube,
        n = 3,
        colours = ['w', 'o', 'g', 'r', 'b', 'y'],
        state = None
    ):
        """
        Input: n - integer representing the width and height of the rubiks struct
               colours - list containing the first letter of ever colour you wish to use (Default = ['w', 'o', 'g', 'r', 'b', 'y']) [OPTIONAL]
               state - string representing the current state of the rubix struct (Default = None) [OPTIONAL]
        Description: Initialize the rubiks struct
        Output: None
        """
        if state is None:
            cube.n = n
            cube.colours = colours
            cube.reset()
        else:
            cube.n = int((len(state) / 6) ** (.5))
            cube.colours = []
            cube.struct = [[[]]]
            for i, s in enumerate(state):
                if s not in cube.colours: cube.colours.append(s)
                cube.struct[-1][-1].append(s)
                if len(cube.struct[-1][-1]) == cube.n and len(cube.struct[-1]) < cube.n:
                    cube.struct[-1].append([])
                elif len(cube.struct[-1][-1]) == cube.n and len(cube.struct[-1]) == cube.n and i < len(state) - 1:
                    cube.struct.append([[]])

    def reset(cube):
        """
        Input: None
        Description: Reset the struct to its inital state
        Output: None
        """
        cube.struct = [[[c for x in range(cube.n)] for y in range(cube.n)] for c in cube.colours]

    def solved(cube):
        """
        Input: None
        Description: Determine if the struct is solved or not
        Output: boolean representing if the struct is solved or not
        """
        for side in cube.struct:
            hold = []
            check = True
            for row in side:
                if len(set(row)) == 1:
                    hold.append(row[0])
                else:
                    check = False
                    break
            if check == False:
                break
            if len(set(hold)) > 1:
                check = False
                break
        return check

    def stringify(cube):
        """
        Input: None
        Description: Create string representation of the current state of the struct
        Output: string representing the struct current state
        """
        return ''.join([i for r in cube.struct for s in r for i in s])

    def shuffle(cube, l_rot = 5, u_rot = 100):
        """
        Input: l_rot - integer representing the lower bounds of amount of moves (Default = 5) [OPTIONAL]
               u_rot - integer representing the upper bounds of amount of moves (Default = 100) [OPTIONAL]
        Description: Shuffles rubiks struct to random solvable state
        Output: None
        """
        moves = randint(l_rot, u_rot)
        moves = 10
        actions = [
            ('h', 0),
            ('h', 1),
            ('v', 0),
            ('v', 1),
            ('s', 0),
            ('s', 1)
        ]
        for i in range(moves):
            a = choice(actions)
            j = randint(0, cube.n - 1)
            if a[0] == 'h':
                print("operation-",a,"row no - ",j)
                #print("row no - ",j)
                cube.horizontal_twist(j, a[1])
                
            elif a[0] == 'v':
                print("operation-",a,"column no -",j)
                cube.vertical_twist(j, a[1])
                #print("column no -",j)
            elif a[0] == 's':
                print("operation-",a,"column no -",j)
                cube.side_twist(j, a[1])
                #print("column no -",j)
        #for i in range(moves):
            # a = choice(actions)
            # j = randint(0, cube.n - 1)
            # if a[0] == 'h':
            #     cube.horizontal_twist(j, a[1])
            # elif a[0] == 'v':
            #     cube.vertical_twist(j, a[1])
            # elif a[0] == 's':
            #     cube.side_twist(j, a[1])

    def show(cube):
        """
        Input: None
        Description: Show the rubiks struct
        Output: None
        """
        spacing = f'{" " * (len(str(cube.struct[0][0])) + 2)}'
        l1 = '\n'.join(spacing + str(c) for c in cube.struct[0])
        l2 = '\n'.join('  '.join(str(cube.struct[i][j]) for i in range(1,5)) for j in range(len(cube.struct[0])))
        l3 = '\n'.join(spacing + str(c) for c in cube.struct[5])
        print(f'{l1}\n\n{l2}\n\n{l3}')

    def horizontal_twist(cube, row, direction):
        """
        Input: row - integer representing which row you would like to twist
               direction - boolean representing if you want to twist right or left [left - 0, right - 1]
        Description: Twist desired row of rubiks struct
        Output: None
        """
        if row < len(cube.struct[0]):
            if direction == 0: #Twist left
                cube.struct[1][row], cube.struct[2][row], cube.struct[3][row], cube.struct[4][row] = (cube.struct[2][row],
                                                                                              cube.struct[3][row],
                                                                                              cube.struct[4][row],
                                                                                              cube.struct[1][row])

            elif direction == 1: #Twist right
                cube.struct[1][row], cube.struct[2][row], cube.struct[3][row], cube.struct[4][row] = (cube.struct[4][row],
                                                                                              cube.struct[1][row],
                                                                                              cube.struct[2][row],
                                                                                              cube.struct[3][row])
            else:
                print(f'ERROR - direction must be 0 (left) or 1 (right)')
                return
            #Rotating connected face
            if direction == 0: #Twist left
                if row == 0:
                    cube.struct[0] = [list(x) for x in zip(*reversed(cube.struct[0]))] #Transpose top
                elif row == len(cube.struct[0]) - 1:
                    cube.struct[5] = [list(x) for x in zip(*reversed(cube.struct[5]))] #Transpose bottom
            elif direction == 1: #Twist right
                if row == 0:
                    cube.struct[0] = [list(x) for x in zip(*cube.struct[0])][::-1] #Transpose top
                elif row == len(cube.struct[0]) - 1:
                    cube.struct[5] = [list(x) for x in zip(*cube.struct[5])][::-1] #Transpose bottom
        else:
            print(f'ERROR - desired row outside of rubiks struct range. Please select a row between 0-{len(cube.struct[0])-1}')
            return

    def vertical_twist(cube, column, direction):
        """
        Input: column - integer representing which column you would like to twist
               direction - boolean representing if you want to twist up or down [down - 0, up - 1]
        Description: Twist desired column of rubiks struct
        Output: None
        """
        if column < len(cube.struct[0]):
            for i in range(len(cube.struct[0])):
                if direction == 0: #Twist down
                    cube.struct[0][i][column], cube.struct[2][i][column], cube.struct[4][-i-1][-column-1], cube.struct[5][i][column] = (cube.struct[4][-i-1][-column-1],
                                                                                                                                cube.struct[0][i][column],
                                                                                                                                cube.struct[5][i][column],
                                                                                                                                cube.struct[2][i][column])
                elif direction == 1: #Twist up
                    cube.struct[0][i][column], cube.struct[2][i][column], cube.struct[4][-i-1][-column-1], cube.struct[5][i][column] = (cube.struct[2][i][column],
                                                                                                                                cube.struct[5][i][column],
                                                                                                                                cube.struct[0][i][column],
                                                                                                                                cube.struct[4][-i-1][-column-1])
                else:
                    print(f'ERROR - direction must be 0 (down) or 1 (up)')
                    return
            #Rotating connected face
            if direction == 0: #Twist down
                if column == 0:
                    cube.struct[1] = [list(x) for x in zip(*cube.struct[1])][::-1] #Transpose left
                elif column == len(cube.struct[0]) - 1:
                    cube.struct[3] = [list(x) for x in zip(*cube.struct[3])][::-1] #Transpose right
            elif direction == 1: #Twist up
                if column == 0:
                    cube.struct[1] = [list(x) for x in zip(*reversed(cube.struct[1]))] #Transpose left
                elif column == len(cube.struct[0]) - 1:
                    cube.struct[3] = [list(x) for x in zip(*reversed(cube.struct[3]))] #Transpose right
        else:
            print(f'ERROR - desired column outside of rubiks struct range. Please select a column between 0-{len(cube.struct[0])-1}')
            return

    def side_twist(cube, column, direction):
        """
        Input: column - integer representing which column you would like to twist
               direction - boolean representing if you want to twist up or down [down - 0, up - 1]
        Description: Twist desired side column of rubiks struct
        Output: None
        """
        if column < len(cube.struct[0]):
            for i in range(len(cube.struct[0])):
                if direction == 0: #Twist down
                    cube.struct[0][column][i], cube.struct[1][-i-1][column], cube.struct[3][i][-column-1], cube.struct[5][-column-1][-1-i] = (cube.struct[3][i][-column-1],
                                                                                                                                      cube.struct[0][column][i],
                                                                                                                                      cube.struct[5][-column-1][-1-i],
                                                                                                                                      cube.struct[1][-i-1][column])
                elif direction == 1: #Twist up
                    cube.struct[0][column][i], cube.struct[1][-i-1][column], cube.struct[3][i][-column-1], cube.struct[5][-column-1][-1-i] = (cube.struct[1][-i-1][column],
                                                                                                                                      cube.struct[5][-column-1][-1-i],
                                                                                                                                      cube.struct[0][column][i],
                                                                                                                                      cube.struct[3][i][-column-1])
                else:
                    print(f'ERROR - direction must be 0 (down) or 1 (up)')
                    return
            #Rotating connected face
            if direction == 0: #Twist down
                if column == 0:
                    cube.struct[4] = [list(x) for x in zip(*reversed(cube.struct[4]))] #Transpose back
                elif column == len(cube.struct[0]) - 1:
                    cube.struct[2] = [list(x) for x in zip(*reversed(cube.struct[2]))] #Transpose top
            elif direction == 1: #Twist up
                if column == 0:
                    cube.struct[4] = [list(x) for x in zip(*cube.struct[4])][::-1] #Transpose back
                elif column == len(cube.struct[0]) - 1:
                    cube.struct[2] = [list(x) for x in zip(*cube.struct[2])][::-1] #Transpose top
        else:
            print(f'ERROR - desired column outside of rubiks struct range. Please select a column between 0-{len(cube.struct[0])-1}')
            return
