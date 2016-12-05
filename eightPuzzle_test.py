from puzzle_heuristics import *

problem = EightPuzzleState("START",0,[1,3,6,5,0,2,4,7,8])

print("Misplaced tiles: {}".format(heur_displaced(problem)))
print("Manhattan distance: {}".format(heur_manhattan_distance(problem)))
print("Out of row and column: {}".format(heur_out_of_row_and_column(problem)))