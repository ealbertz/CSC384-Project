from puzzle_heuristics import *
from eightPuzzle import *
from fifteenPuzzle import *
from idastar import *
import csv

#DFS, BFS, A*, IDA*

result_file = open('result.txt','wb')

with open("result.csv", "w", newline="") as result_file:
	wr = csv.writer(result_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
	wr.writerow(['Puzzle size', 'Problem', 'Strategy', 'Heuristic', 'Result', 'Time', 'Cost', 'Nodes expanded', 'States expanded'])

	for i in range(0,20):
		print("******************************")
		print("PROBLEM {}".format(i+1))
		s0 = EIGHT_PROBLEMS[i]

		print("----- BFS -----")
		se = SearchEngine('breadth_first', 'full')
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, timebound = 5)
		if (final):
			wr.writerow(['8', i+1, 'BFS', '', 'Success', str(se.total_search_time), str(final.gval), sNode.n, StateSpace.n])
		else:
			wr.writerow(['8', i+1, 'BFS', '', 'Failure', '', '', sNode.n, StateSpace.n])
		
		print("----- DFS -----")
		se = SearchEngine('depth_first', 'path')
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, timebound = 5)
		if (final):
			wr.writerow(['8', i+1, 'DFS', '', 'Success', str(se.total_search_time), str(final.gval), sNode.n, StateSpace.n])
		else:
			wr.writerow(['8', i+1, 'DFS', '', 'Failure', '', '', sNode.n, StateSpace.n])

		print("----- A* with Manhattan -----")
		se = SearchEngine('astar', 'full')
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_manhattan_distance, timebound = 5)
		if (final):
			wr.writerow(['8', i+1, 'A*', 'Manhattan', 'Success', str(se.total_search_time), str(final.gval), sNode.n, StateSpace.n])
		else:
			wr.writerow(['8', i+1, 'A*', 'Manhattan', 'Failure', '', '', sNode.n, StateSpace.n])

		print("----- A* with Manhattan + Linear Conflict -----")
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_manhattan_linear, timebound = 5)
		if (final):
			wr.writerow(['8', i+1, 'A*', 'Manhattan & Linear', 'Success', str(se.total_search_time), str(final.gval), sNode.n, StateSpace.n])
		else:
			wr.writerow(['8', i+1, 'A*', 'Manhattan & Linear', 'Failure', '', '', sNode.n, StateSpace.n])

		print("----- A* with Out of Row and Column -----")
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_out_of_row_and_column, timebound = 5)
		if (final):
			wr.writerow(['8', i+1, 'A*', 'Out of Row and Column', 'Success', str(se.total_search_time), str(final.gval), sNode.n, StateSpace.n])
		else:
			wr.writerow(['8', i+1, 'A*', 'Out of Row and Column', 'Failure', '', '', sNode.n, StateSpace.n])

		print("----- A* with Misplaced Tiles -----")
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_misplaced, timebound = 5)
		if (final):
			wr.writerow(['8', i+1, 'A*', 'Misplaced', 'Success', str(se.total_search_time), str(final.gval), sNode.n, StateSpace.n])
		else:
			wr.writerow(['8', i+1, 'A*', 'Misplaced', 'Failure', '', '', sNode.n, StateSpace.n])

		print("----- IDA* with Manhattan -----")
		final, total_time = iterative_deepening_astar(initial_state = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_manhattan_distance, timebound = 5)
		if (final):
			wr.writerow(['8', i+1, 'IDA*', 'Manhattan', 'Success', total_time, str(final.gval), sNode.n, StateSpace.n])
		else:
			wr.writerow(['8', i+1, 'IDA*', 'Manhattan', 'Failure', total_time, '', sNode.n, StateSpace.n])

		print("----- IDA* with Manhattan + Linear Conflict -----")
		final, total_time = iterative_deepening_astar(initial_state = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_manhattan_linear, timebound = 5)
		if (final):
			wr.writerow(['8', i+1, 'IDA*', 'Manhattan & Linear', 'Success', total_time, str(final.gval), sNode.n, StateSpace.n])
		else:
			wr.writerow(['8', i+1, 'IDA*', 'Manhattan & Linear', 'Failure', total_time, '', sNode.n, StateSpace.n])

		print("----- IDA* with Out of Row and Column -----")
		final, total_time = iterative_deepening_astar(initial_state = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_out_of_row_and_column, timebound = 5)
		if (final):
			wr.writerow(['8', i+1, 'IDA*', 'Out of Row and Column', 'Success', total_time, str(final.gval), sNode.n, StateSpace.n])
		else:
			wr.writerow(['8', i+1, 'IDA*', 'Out of Row and Column', 'Failure', total_time, '', sNode.n, StateSpace.n])

		print("----- IDA* with Misplaced Tiles -----")
		final, total_time = iterative_deepening_astar(initial_state = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_misplaced, timebound = 5)
		if (final):
			wr.writerow(['8', i+1, 'IDA*', 'Misplaced', 'Success', total_time, str(final.gval), sNode.n, StateSpace.n])
		else:
			wr.writerow(['8', i+1, 'IDA*', 'Misplaced', 'Failure', total_time, '', sNode.n, StateSpace.n])

	for i in range(0,5):
		print("******************************")
		print("PROBLEM {}".format(i+1))
		s0 = FIFTEEN_PROBLEMS[i]

		print("----- BFS -----")
		se = SearchEngine('breadth_first', 'full')
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, timebound = 5)
		if (final):
			wr.writerow(['15', i+1, 'BFS', '', 'Success', str(se.total_search_time), str(final.gval), sNode.n, StateSpace.n])
		else:
			wr.writerow(['15', i+1, 'BFS', '', 'Failure', '', '', sNode.n, StateSpace.n])
		
		print("----- DFS -----")
		se = SearchEngine('depth_first', 'path')
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, timebound = 5)
		if (final):
			wr.writerow(['15', i+1, 'DFS', '', 'Success', str(se.total_search_time), str(final.gval), sNode.n, StateSpace.n])
		else:
			wr.writerow(['15', i+1, 'DFS', '', 'Failure', '', '', sNode.n, StateSpace.n])

		print("----- A* with Manhattan -----")
		se = SearchEngine('astar', 'full')
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_manhattan_distance, timebound = 5)
		if (final):
			wr.writerow(['15', i+1, 'A*', 'Manhattan', 'Success', str(se.total_search_time), str(final.gval), sNode.n, StateSpace.n])
		else:
			wr.writerow(['15', i+1, 'A*', 'Manhattan', 'Failure', '', '', sNode.n, StateSpace.n])

		print("----- A* with Manhattan + Linear Conflict -----")
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_manhattan_linear, timebound = 5)
		if (final):
			wr.writerow(['15', i+1, 'A*', 'Manhattan & Linear', 'Success', str(se.total_search_time), str(final.gval), sNode.n, StateSpace.n])
		else:
			wr.writerow(['15', i+1, 'A*', 'Manhattan & Linear', 'Failure', '', '', sNode.n, StateSpace.n])

		print("----- A* with Out of Row and Column -----")
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_out_of_row_and_column, timebound = 5)
		if (final):
			wr.writerow(['15', i+1, 'A*', 'Out of Row and Column', 'Success', str(se.total_search_time), str(final.gval), sNode.n, StateSpace.n])
		else:
			wr.writerow(['15', i+1, 'A*', 'Out of Row and Column', 'Failure', '', '', sNode.n, StateSpace.n])

		print("----- A* with Misplaced Tiles -----")
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_misplaced, timebound = 5)
		if (final):
			wr.writerow(['15', i+1, 'A*', 'Misplaced', 'Success', str(se.total_search_time), str(final.gval), sNode.n, StateSpace.n])
		else:
			wr.writerow(['15', i+1, 'A*', 'Misplaced', 'Failure', '', '', sNode.n, StateSpace.n])

		print("----- IDA* with Manhattan -----")
		final, total_time = iterative_deepening_astar(initial_state = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_manhattan_distance, timebound = 5)
		if (final):
			wr.writerow(['15', i+1, 'IDA*', 'Manhattan', 'Success', total_time, str(final.gval), sNode.n, StateSpace.n])
		else:
			wr.writerow(['15', i+1, 'IDA*', 'Manhattan', 'Failure', total_time, '', sNode.n, StateSpace.n])

		print("----- IDA* with Manhattan + Linear Conflict -----")
		final, total_time = iterative_deepening_astar(initial_state = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_manhattan_linear, timebound = 5)
		if (final):
			wr.writerow(['15', i+1, 'IDA*', 'Manhattan & Linear', 'Success', total_time, str(final.gval), sNode.n, StateSpace.n])
		else:
			wr.writerow(['15', i+1, 'IDA*', 'Manhattan & Linear', 'Failure', total_time, '', sNode.n, StateSpace.n])

		print("----- IDA* with Out of Row and Column -----")
		final, total_time = iterative_deepening_astar(initial_state = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_out_of_row_and_column, timebound = 5)
		if (final):
			wr.writerow(['15', i+1, 'IDA*', 'Out of Row and Column', 'Success', total_time, str(final.gval), sNode.n, StateSpace.n])
		else:
			wr.writerow(['15', i+1, 'IDA*', 'Out of Row and Column', 'Failure', total_time, '', sNode.n, StateSpace.n])

		print("----- IDA* with Misplaced Tiles -----")
		final, total_time = iterative_deepening_astar(initial_state = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_misplaced, timebound = 5)
		if (final):
			wr.writerow(['15', i+1, 'IDA*', 'Misplaced', 'Success', total_time, str(final.gval), sNode.n, StateSpace.n])
		else:
			wr.writerow(['15', i+1, 'IDA*', 'Misplaced', 'Failure', total_time, '', sNode.n, StateSpace.n])

		'''
		TODO-list:
		Lägg till fler 15-pussel
		ändra tiden (främst för 15)
		lägg till weighted A* från A1?
		Ändra IDA* så att den inte går över tidsgränsen'''

