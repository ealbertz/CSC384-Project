from puzzle_heuristics import *
from eightPuzzle import *


for i in range(0,20):
	print("******************************")
	print("PROBLEM {}".format(i+1))
	s0 = EIGHT_PROBLEMS[i]
	se = SearchEngine('best_first', 'full')
	for h in [heur_displaced, heur_manhattan_distance,heur_out_of_row_and_column]:
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, heur_fn = h, timebound = 1)
