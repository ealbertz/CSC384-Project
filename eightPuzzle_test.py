from puzzle_heuristics import *

problem = FifteenPuzzleState("START",0,[1,3,6,5,0,2,4,7,8,9,10,11,12,13,14,15])

print("Misplaced tiles: {}".format(heur_displaced(problem)))
print("Manhattan distance: {}".format(heur_manhattan_distance(problem)))
print("Out of row and column: {}".format(heur_out_of_row_and_column(problem)))