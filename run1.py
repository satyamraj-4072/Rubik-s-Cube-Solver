from cube_basics import *

cube = RubiksCube(n=3)
cube.shuffle(l_rot =5,u_rot =14)
print(cube.stringify())