from search import * #for search engines
from eightPuzzle import *
from fifteenPuzzle import *
from math import * #for sqrt function

def heur_misplaced(state):      
  
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
      if (linear_conflict(state.state.index(tj), state.state.index(tk), state.goal_state.index(tj), state.goal_state.index(tk), sqrt(n)) or linear_conflict(state.state.index(tk), state.state.index(tj), state.goal_state.index(tk), state.goal_state.index(tj), sqrt(n))):
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
