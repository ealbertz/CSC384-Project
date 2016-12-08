from search import * #for search engines
from eightPuzzle import *
from fifteenPuzzle import *

def iterative_deepening_astar(initial_state, goal_fn, heur_fn, timebound):

	se = SearchEngine('depth_first', 'full')

	current_bound = 1
	current_timebound = timebound
	solution = False
	total_time = 0

	while (current_timebound): #while we are not in a goal node
		solution = se.search(initState = initial_state, goal_fn = goal_fn, heur_fn = heur_fn, bound = current_bound, timebound = current_timebound)

		total_time += se.total_search_time
		current_timebound = max(0, current_timebound - se.total_search_time)
		current_bound = se.smallestNotExplored

		if (solution):
			return solution, total_time
		
	return False, total_time

