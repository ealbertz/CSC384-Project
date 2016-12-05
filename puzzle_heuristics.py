from search import * #for search engines
from sokoban import SokobanState, Direction, PROBLEMS, sokoban_goal_state #for Sokoban specific classes and problems


def heur_displaced(state):      
  
  count = 0
  for i in range (1,state.state.length - 1):
    if state.state.index(i) != state.goal_state.index(i):
      count += 1
  return count

def heur_manhattan_distance(state):
'''A heuristic function which returns the sum of all Manhattan distances for each tile to its goal position'''

  n = state.state.length - 1 #The width/height of the puzzle
  total_dist = 0
  for i in range (1,n):
   total_dist += manhattan_dist(state.state.index(i),state.goal_state.index(i),n)
  return total_dist

def manhattan_dist(i,j,n)
'''Manhattan distance of two indexes i and j in a puzzle with the width/height n'''
  return abs(i % n - j % n) + abs(i // n - j // n)

def heur_alternate(state):
#IMPLEMENT
    '''a better sokoban heuristic'''
    '''INPUT: a sokoban state'''
    '''OUTPUT: a numeric value that serves as an estimate of the distance of the state to the goal.'''        
    #heur_min_moves has flaws.   
    #Write a heuristic function that improves upon heur_manhattan_distance to estimate distance between the current state and the goal.
    #Your function should return a numeric value for the estimate of the distance to the goal.

    # This heuristic returns the Manhattan distance of the boxes to their closest storage space, but only one box can be "stored" in each storage. This means that when one box has used a storage spot as its closest storage, no other box can use it.

    total_dist = 0

    available_storage = set(state.storage)
    for box in state.boxes:
      min_dist = float('inf')
      for storage in available_storage:
          dist = abs(box[0]-storage[0]) + abs(box[1]-storage[1])
          if dist < min_dist:
            min_dist = dist
            min_storage = storage
      available_storage.remove(min_storage)
      total_dist += min_dist

    return total_dist

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

def weighted_astar(initial_state, timebound = 10):
#IMPLEMENT
    '''Provides an implementation of weighted a-star, as described in the HW1 handout'''
    '''INPUT: a sokoban state that represents the start state and a timebound (number of seconds)'''
    '''OUTPUT: A goal state (if a goal is found), else False'''
    se = SearchEngine('custom','full')
    current_weight = 1
    current_timebound = timebound
    final = False
    while (current_timebound and current_weight >= 0):
        current_result = se.search(initState = initial_state, heur_fn = heur_alternate, timebound = current_timebound, goal_fn = sokoban_goal_state, fval_function = fval_function, weight = current_weight)
        if (current_result):
          final = current_result
        current_weight -= 0.3
        current_timebound = max(0,current_timebound - se.total_search_time)
    return final

if __name__ == "__main__":
  #TEST CODE
  solved = 0; unsolved = []; counter = 0; percent = 0; timebound = 2; #2 second time limit for each problem
  print("*************************************")  
  print("Running A-star")     

  for i in range(0,0): #note that there are 40 problems in the set that has been provided.  We just run through 10 here for illustration.

    print("*************************************")  
    print("PROBLEM {}".format(i))
    
    s0 = PROBLEMS[i] #Problems will get harder as i gets bigger

    se = SearchEngine('astar', 'full')
    final = se.search(s0, sokoban_goal_state, heur_displaced, timebound)

    if final:
      final.print_path()
      solved += 1
    else:
      unsolved.append(i)    
    counter += 1

  if counter > 0:  
    percent = (solved/counter)*100

  print("*************************************")  
  print("{} of {} problems ({} %) solved in less than {} seconds.".format(solved, counter, percent, timebound))  
  print("Problems that remain unsolved in the set are Problems: {}".format(unsolved))      
  print("*************************************") 

  solved = 0; unsolved = []; counter = 0; percent = 0; timebound = 8; #8 second time limit 
  print("Running Anytime Weighted A-star")   

  for i in range(0,40):
    print("*************************************")  
    print("PROBLEM {}".format(i))

    s0 = PROBLEMS[i] #Problems get harder as i gets bigger
    final = weighted_astar(s0, timebound)

    if final:
      final.print_path()   
      solved += 1 
    else:
      unsolved.append(i)
    counter += 1      

  if counter > 0:  
    percent = (solved/counter)*100   
      
  print("*************************************")  
  print("{} of {} problems ({} %) solved in less than {} seconds.".format(solved, counter, percent, timebound))  
  print("Problems that remain unsolved in the set are Problems: {}".format(unsolved))      
  print("*************************************") 


