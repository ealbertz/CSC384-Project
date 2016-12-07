from search import * #for search engines
from eightPuzzle import *
from fifteenPuzzle import *

def fval_function(sN, weight): 

  gval=sN.gval
  hval=sN.hval
  fval= gval+hval
  
  return fval



def iterative_deepening_astar(initial_state, goal_fn, heur_fn, timebound):

	se=SearchEngine('depth_first', 'full')
	curBound=1
	solution=False
	total_time = 0
	while(solution == False): #while we are not in a goal node
		solution = se.search(initState=initial_state, goal_fn = goal_fn, heur_fn = heur_fn, fval_function=fval_function, bound=curBound, timebound=timebound)
		total_time += se.total_search_time
		if(solution == False):
			if (total_time >= timebound):
				return False
			smallestNotExplored=se.smallestNotExplored
			print(se.smallestNotExplored)
			curBound=smallestNotExplored
	print("Total time: {}".format(total_time))
	return solution, total_time

