from search import * #for search engines
from eightPuzzle import *
from fifteenPuzzle import *
from math import * #for sqrt function

def heur_displaced(state):      
  
  count = 0
  for i in range (1,len(state.state)):
    if state.state.index(i) != state.goal_state.index(i):
      count += 1
  return count

def heur_manhattan_distance(state):
  '''A heuristic function which returns the sum of all Manhattan distances for each tile to its goal position.'''

  n = len(state.state) #The number of tiles in the puzzle
  total_dist = 0
  for i in range (1,n):
   total_dist += manhattan_dist(state.state.index(i),state.goal_state.index(i),sqrt(n))
  return total_dist

def manhattan_dist(i,j,n):
  '''Manhattan distance of two indexes i and j in a puzzle with the width/height n.'''
  return abs(i % n - j % n) + abs(i // n - j // n)

def heur_out_of_row_and_column(state):
  '''A heuristic function which returns the sum of number of tiles in the wrong row and the number of tiles in the wrong column.'''
  
  n = len(state.state) #The number of tiles in the puzzle
  count = 0
  for i in range(1,n):
    if state.state.index(i) % sqrt(n) != state.goal_state.index(i) % sqrt(n):
      count += 1
    if state.state.index(i) // sqrt(n) != state.goal_state.index(i) // sqrt(n):
      count += 1
  return count

def heur_linear_conflict(state):
  '''A heuristic function which returns the number of tiles that are in linear conflict.'''

  n = len(state.state) #The number of tiles in the puzzle

  count = 0

  for tj in range (1,n):
    for tk in range (tj+1,n):
      if (linear_conflict(state.state.index(tj), state.state.index(tk), state.goal_state.index(tj), state.goal_state.index(tk), sqrt(n))):
        count += 2

  return count

def heur_manhattan_linear(state):
  return heur_manhattan_distance(state) + heur_linear_conflict(state)

def linear_conflict(tj, tk, tj_goal, tk_goal, n):
  '''Two tiles tj and tk are in a linear conflict if tj and tk are in the same line, 
  the goal positions of tj and tk are both in that line, 
  tj is to the right of tk and goal position of tj is to the left of the goal position of tk.

  n is the width/height of the puzzle.'''

  if tj // n == tk // n: #Tiles are on the same row
    return tj // n == tj_goal // n and tj_goal // n == tk_goal // n and tj > tk and tj_goal < tk_goal
  elif tj % n == tk % n: #Tiles are in the same column
    return tj % n == tj_goal % n and tj_goal % n == tk_goal % n and tj > tk and tj_goal < tk_goal
  else:
    return False

def fval_function(sN, weight):
#IMPLEMENT
    """
    Provide a custom formula for f-value computation for Anytime Weighted A star.
    Returns the fval of the state contained in the sNode.

    @param sNode sN: A search node (containing a SokobanState)
    @param float weight: Weight given by Anytime Weighted A star
    @rtype: float
    """
  
    #Many searches will explore nodes (or states) that are ordered by their f-value.
    #For UCS, the fvalue is the same as the gval of the state. For best-first search, the fvalue is the hval of the state.
    #You can use this function to create an alternate f-value for states; this must be a function of the state and the weight.
    #The function must return a numeric f-value.
    #The value will determine your state's position on the Frontier list during a 'custom' search.
    #You must initialize your search engine object as a 'custom' search engine if you supply a custom fval function.
    return (1 - weight) * sN.gval + weight * sN.hval

'''problem = EightPuzzleState("START",0,[1,3,2,4,8,6,7,5,0])
problem.print_state()

print("Linear conflicts: {}".format(heur_linear_conflict(problem)))'''
