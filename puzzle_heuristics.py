from search import * #for search engines
from eightPuzzle import *

def heur_displaced(state):      
  
  count = 0
  for i in range (1,state.state.length - 1):
    if state.state.index(i) != state.goal_state.index(i):
      count += 1
  return count

def heur_manhattan_distance(state):
'''A heuristic function which returns the sum of all Manhattan distances for each tile to its goal position'''

  n = state.state.length - 1 #The number of tiles in the puzzle
  total_dist = 0
  for i in range (1,n):
   total_dist += manhattan_dist(state.state.index(i),state.goal_state.index(i),sqrt(n + 1))
  return total_dist

def manhattan_dist(i,j,n)
'''Manhattan distance of two indexes i and j in a puzzle with the width/height n'''
  return abs(i % n - j % n) + abs(i // n - j // n)

def heur_out_of_row_and_column(state):
'''A heuristic function which returns the sum of number of tiles in the wrong row and the number of tiles in the wrong column'''
  
  n = state.state.length - 1 #The number of tiles in the puzzle
  count = 0
  for i in range(1,n):
    if state.state.index(i) % sqrt(n) != state.goal_state.index(i) % sqrt(n):
      count += 1
    if state.state.index(i) // sqrt(n) != state.goal_state.index(i) // sqrt(n):
      count += 1
  return count