from puzzle_heuristics import *
from eightPuzzle import *
from fifteenPuzzle import *
from idastar import *
import csv

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
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, timebound = 20)
		if (final):
			wr.writerow(['8', i+1, 'BFS', 'Uninformed', 'Success', se.total_search_time, final.gval, sNode.n, StateSpace.n])
		else:
			wr.writerow(['8', i+1, 'BFS', 'Uninformed', 'Failure', se.total_search_time, -1, sNode.n, StateSpace.n])
		
		print("----- DFS -----")
		se = SearchEngine('depth_first', 'full')
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, timebound = 20)
		if (final):
			wr.writerow(['8', i+1, 'DFS', 'Uninformed', 'Success', se.total_search_time, final.gval, sNode.n, StateSpace.n])
		else:
			wr.writerow(['8', i+1, 'DFS', 'Uninformed', 'Failure', se.total_search_time, -1, sNode.n, StateSpace.n])

		print("----- A* with Manhattan -----")
		se = SearchEngine('astar', 'full')
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_manhattan_distance, timebound = 20)
		if (final):
			wr.writerow(['8', i+1, 'A*', 'Manhattan', 'Success', se.total_search_time, final.gval, sNode.n, StateSpace.n])
		else:
			wr.writerow(['8', i+1, 'A*', 'Manhattan', 'Failure', se.total_search_time, -1, sNode.n, StateSpace.n])

		print("----- A* with Manhattan + Linear Conflict -----")
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_manhattan_linear, timebound = 20)
		if (final):
			wr.writerow(['8', i+1, 'A*', 'Manhattan & Linear', 'Success', se.total_search_time, final.gval, sNode.n, StateSpace.n])
		else:
			wr.writerow(['8', i+1, 'A*', 'Manhattan & Linear', 'Failure', se.total_search_time, -1, sNode.n, StateSpace.n])

		print("----- A* with Out of Row and Column -----")
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_out_of_row_and_column, timebound = 20)
		if (final):
			wr.writerow(['8', i+1, 'A*', 'Out of Row and Column', 'Success', se.total_search_time, final.gval, sNode.n, StateSpace.n])
		else:
			wr.writerow(['8', i+1, 'A*', 'Out of Row and Column', 'Failure', se.total_search_time, -1, sNode.n, StateSpace.n])

		print("----- A* with Misplaced Tiles -----")
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_misplaced, timebound = 20)
		if (final):
			wr.writerow(['8', i+1, 'A*', 'Misplaced', 'Success', se.total_search_time, final.gval, sNode.n, StateSpace.n])
		else:
			wr.writerow(['8', i+1, 'A*', 'Misplaced', 'Failure', se.total_search_time, -1, sNode.n, StateSpace.n])

		print("----- IDA* with Manhattan -----")
		final, total_time = iterative_deepening_astar(initial_state = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_manhattan_distance, timebound = 20)
		if (final):
			wr.writerow(['8', i+1, 'IDA*', 'Manhattan', 'Success', total_time, final.gval, sNode.n, StateSpace.n])
		else:
			wr.writerow(['8', i+1, 'IDA*', 'Manhattan', 'Failure', total_time, -1, sNode.n, StateSpace.n])

		print("----- IDA* with Manhattan + Linear Conflict -----")
		final, total_time = iterative_deepening_astar(initial_state = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_manhattan_linear, timebound = 20)
		if (final):
			wr.writerow(['8', i+1, 'IDA*', 'Manhattan & Linear', 'Success', total_time, final.gval, sNode.n, StateSpace.n])
		else:
			wr.writerow(['8', i+1, 'IDA*', 'Manhattan & Linear', 'Failure', total_time, -1, sNode.n, StateSpace.n])

		print("----- IDA* with Out of Row and Column -----")
		final, total_time = iterative_deepening_astar(initial_state = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_out_of_row_and_column, timebound = 20)
		if (final):
			wr.writerow(['8', i+1, 'IDA*', 'Out of Row and Column', 'Success', total_time, final.gval, sNode.n, StateSpace.n])
		else:
			wr.writerow(['8', i+1, 'IDA*', 'Out of Row and Column', 'Failure', total_time, -1, sNode.n, StateSpace.n])

		print("----- IDA* with Misplaced Tiles -----")
		final, total_time = iterative_deepening_astar(initial_state = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_misplaced, timebound = 20)
		if (final):
			wr.writerow(['8', i+1, 'IDA*', 'Misplaced', 'Success', total_time, final.gval, sNode.n, StateSpace.n])
		else:
			wr.writerow(['8', i+1, 'IDA*', 'Misplaced', 'Failure', total_time, -1, sNode.n, StateSpace.n])

	for i in range(0,15):
		print("******************************")
		print("PROBLEM {}".format(i+1))
		s0 = FIFTEEN_PROBLEMS[i]

		print("----- BFS -----")
		se = SearchEngine('breadth_first', 'full')
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, timebound = 20)
		if (final):
			wr.writerow(['15', i+1, 'BFS', 'Uninformed', 'Success', se.total_search_time, final.gval, sNode.n, StateSpace.n])
		else:
			wr.writerow(['15', i+1, 'BFS', 'Uninformed', 'Failure', se.total_search_time, -1, sNode.n, StateSpace.n])
		
		print("----- DFS -----")
		se = SearchEngine('depth_first', 'full')
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, timebound = 20)
		if (final):
			wr.writerow(['15', i+1, 'DFS', 'Uninformed', 'Success', se.total_search_time, final.gval, sNode.n, StateSpace.n])
		else:
			wr.writerow(['15', i+1, 'DFS', 'Uninformed', 'Failure', se.total_search_time, -1, sNode.n, StateSpace.n])

		print("----- A* with Manhattan -----")
		se = SearchEngine('astar', 'full')
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_manhattan_distance, timebound = 20)
		if (final):
			wr.writerow(['15', i+1, 'A*', 'Manhattan', 'Success', se.total_search_time, final.gval, sNode.n, StateSpace.n])
		else:
			wr.writerow(['15', i+1, 'A*', 'Manhattan', 'Failure', se.total_search_time, -1, sNode.n, StateSpace.n])

		print("----- A* with Manhattan + Linear Conflict -----")
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_manhattan_linear, timebound = 20)
		if (final):
			wr.writerow(['15', i+1, 'A*', 'Manhattan & Linear', 'Success', se.total_search_time, final.gval, sNode.n, StateSpace.n])
		else:
			wr.writerow(['15', i+1, 'A*', 'Manhattan & Linear', 'Failure', se.total_search_time, -1, sNode.n, StateSpace.n])

		print("----- A* with Out of Row and Column -----")
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_out_of_row_and_column, timebound = 20)
		if (final):
			wr.writerow(['15', i+1, 'A*', 'Out of Row and Column', 'Success', se.total_search_time, final.gval, sNode.n, StateSpace.n])
		else:
			wr.writerow(['15', i+1, 'A*', 'Out of Row and Column', 'Failure', se.total_search_time, -1, sNode.n, StateSpace.n])

		print("----- A* with Misplaced Tiles -----")
		final = se.search(initState = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_misplaced, timebound = 20)
		if (final):
			wr.writerow(['15', i+1, 'A*', 'Misplaced', 'Success', se.total_search_time, final.gval, sNode.n, StateSpace.n])
		else:
			wr.writerow(['15', i+1, 'A*', 'Misplaced', 'Failure', se.total_search_time, -1, sNode.n, StateSpace.n])

		print("----- IDA* with Manhattan -----")
		final, total_time = iterative_deepening_astar(initial_state = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_manhattan_distance, timebound = 20)
		if (final):
			wr.writerow(['15', i+1, 'IDA*', 'Manhattan', 'Success', total_time, final.gval, sNode.n, StateSpace.n])
		else:
			wr.writerow(['15', i+1, 'IDA*', 'Manhattan', 'Failure', total_time, -1, sNode.n, StateSpace.n])

		print("----- IDA* with Manhattan + Linear Conflict -----")
		final, total_time = iterative_deepening_astar(initial_state = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_manhattan_linear, timebound = 20)
		if (final):
			wr.writerow(['15', i+1, 'IDA*', 'Manhattan & Linear', 'Success', total_time, final.gval, sNode.n, StateSpace.n])
		else:
			wr.writerow(['15', i+1, 'IDA*', 'Manhattan & Linear', 'Failure', total_time, -1, sNode.n, StateSpace.n])

		print("----- IDA* with Out of Row and Column -----")
		final, total_time = iterative_deepening_astar(initial_state = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_out_of_row_and_column, timebound = 20)
		if (final):
			wr.writerow(['15', i+1, 'IDA*', 'Out of Row and Column', 'Success', total_time, final.gval, sNode.n, StateSpace.n])
		else:
			wr.writerow(['15', i+1, 'IDA*', 'Out of Row and Column', 'Failure', total_time, -1, sNode.n, StateSpace.n])

		print("----- IDA* with Misplaced Tiles -----")
		final, total_time = iterative_deepening_astar(initial_state = s0, goal_fn = eightPuzzle_goal_state, heur_fn = heur_misplaced, timebound = 20)
		if (final):
			wr.writerow(['15', i+1, 'IDA*', 'Misplaced', 'Success', total_time, final.gval, sNode.n, StateSpace.n])
		else:
			wr.writerow(['15', i+1, 'IDA*', 'Misplaced', 'Failure', total_time, -1, sNode.n, StateSpace.n])

print("******************************")
print("All done")
print("******************************")

