
#importing libararies to handle the heuristic database in a json format file 
import json # to store the db into a json format 
import os.path # to access and do CRUD on the json file 

from cube_basics import RubiksCube
from cube_solver import IDA_star, build_heuristic_db, kociemba_solv


MAX_MOVES = 6 # indicates the max no of steps in the heuritic db 
NEW_HEURISTICS = False # not nessesary 
HEURISTIC_FILE = 'heuristic.json'  # naming and creating a new json format file 

#--------------------------------

choice1 = int(input("Do you want to generate a new cube or do you want to input cube as a string \nnew cube->1\nuser cube->0\n:"))
# choice1= 0
if(choice1==1):
        cube = RubiksCube(n=3)   # creating the cube 
        cube.show()   # should be a solved and fresh new cube 
        print('------------------------------------------------0')
        print("<-------------Shuffling the cube--------------->")
        cube.shuffle(l_rot = MAX_MOVES if MAX_MOVES < 5 else 5,u_rot = 14)
        cube.show()
        print('----------')
elif(choice1==0):
        # print("enter the string for the cube state ")
        state = input("enter the string for the cube state ")
        cube = RubiksCube(n=3,state = state )
        cube.show()   # should be a solved and fresh new cube 
        print('-----------')
else:
        print("Error invalid response")

#--------------------------------
"""
    building the database 
""" 
if os.path.exists(HEURISTIC_FILE):    # checks for a pre existing db if present  or not 
    with open(HEURISTIC_FILE) as f:
        h_db = json.load(f)     # if present loads the file 
else:
    h_db = None     # if not present marks as none 

if h_db is None or NEW_HEURISTICS is True:      # if h_db == none create a new DB 
    actions = [(r, n, d) for r in ['h', 'v', 's'] for d in [0, 1] for n in range(cube.n)]   # initialize all the 18 moves that can be done and passes into the build heuristic function 
    #builds the database as per user     
    h_db = build_heuristic_db(
        cube.stringify(),
        actions,
        max_moves = MAX_MOVES,
        heuristic = h_db
    )
    #storing the db into the file
    with open(HEURISTIC_FILE, 'w', encoding='utf-8') as f:
        json.dump(
            h_db,
            f,
            ensure_ascii=False,
            indent=4
        )
#--------------------------------implementing the solver 
solver = IDA_star(h_db) # creating an instance of the solver class 
moves = solver.run(cube.stringify()) # getting the moves to solve the cube 
print(moves)
print('-----------')
# implementing the moves to step by step solve the cube
for m in moves:
    if m[0] == 'h':
        cube.horizontal_twist(m[1], m[2])
        cube.show()
        print('-----------')
    elif m[0] == 'v':
        cube.vertical_twist(m[1], m[2])
        cube.show()
        print('-----------')
    elif m[0] == 's':
        cube.side_twist(m[1], m[2])
        cube.show()
        print('-----------')
cube.show()

