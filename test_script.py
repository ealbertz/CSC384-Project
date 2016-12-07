from puzzle_heuristics import *
from eightPuzzle import *
from fifteenPuzzle import *
from idastar import *

for i in range(0,20):
	print("******************************")
	print("PROBLEM {}".format(i+1))
	s0 = EIGHT_PROBLEMS[i]
	se = SearchEngine('astar', 'full')
	for h in [heur_displaced, heur_manhattan_distance,heur_out_of_row_and_column, heur_manhattan_linear]:
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, heur_fn = h, timebound = 1)

for i in range(0,5):
	print("******************************")
	print("PROBLEM {}".format(i+1))
	s0 = FIFTEEN_PROBLEMS[i]
	se = SearchEngine('astar', 'full')
	for h in [heur_displaced, heur_manhattan_distance,heur_out_of_row_and_column, heur_manhattan_linear]:
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, heur_fn = h, timebound = 5)

iterative_deepening_astar(EIGHT_PROBLEMS[0], eightPuzzle_goal_state, heur_manhattan_distance)
