
'''Statespace 8-Puzzle
'''
from search import *

class EightPuzzleState(StateSpace):
    StateSpace.n=0

    def __init__(self, action, gval, state, parent = None):
        '''Create an puzzle stae object. The  input parameter state represents the puzzle as a list of numbers in teh range[0-8],
        where zero represents the blank tile.
        '''

        StateSpace.__init__(self, action,gval,parent)
        self.state=state
        self.goal_state = [1,2,3,4,5,6,7,8,0]

    def successors(self):
        '''
        Generates all actions that can be performed from this state, and the states those actions will create. 
        '''
        successors=[]
        transition_cost =1
        position_blank=self.state.index(0)

        if position_blank < 6: #possible to slide blank tile down
            state = self.state[:]
            state[position_blank] = state[position_blank+3]
            state[position_blank + 3] = 0 
            new_state = EightPuzzleState("Blank down", self.gval+transition_cost, state, self)
            successors.append(new_state)
        if position_blank > 2: #possible to slide blank tile up
            state = self.state[:]
            state[position_blank] = state[position_blank-3]
            state[position_blank - 3] = 0 
            new_state = EightPuzzleState("Blank up", self.gval+transition_cost, state, self)
            successors.append(new_state)

        if position_blank % 3 < 2: #possible to slide blank tile right
            state = self.state[:]
            state[position_blank] = state[position_blank+1]
            state[position_blank + 1] = 0 
            new_state = EightPuzzleState("Blank right", self.gval+transition_cost, state, self)
            successors.append(new_state)

        if position_blank % 3 > 0: #possible to slide blank tile left
            state = self.state[:]
            state[position_blank] = state[position_blank-1]
            state[position_blank -1] = 0 
            new_state = EightPuzzleState("Blank left", self.gval+transition_cost, state, self)
            successors.append(new_state)

        return successors



    def hashable_state(self):
        return tuple(self.state)


    def print_state(self):
        if self.parent:
            print("Action= \"{}\", S{}, g-value = {}, (From S{})".format(self.action, self.index, self.gval, self.parent.index))
        else:
            print("Action= \"{}\", S{}, g-value = {}, (Initial State)".format(self.action, self.index, self.gval))


        print("|-----------|")
        print("| {} | {} | {} |".format(self.state[0],self.state[1],self.state[2]))
        print("|-----------|")
        print("| {} | {} | {} |".format(self.state[3],self.state[4],self.state[5]))
        print("|-----------|")
        print("| {} | {} | {} |".format(self.state[6],self.state[7],self.state[8]))
        print("|-----------|")


def eightPuzzle_goal_state(state):
    '''Returns true if we have reached a goal state'''
    '''Input: an eightPuzzle state'''
    '''Output: True (if goal) or False (if not)'''
    return(state.goal_state == state.state)

'''A set of problems for the 8-puzzle'''
EIGHT_PROBLEMS = (
    EightPuzzleState("START",0,[2,0,4,5,8,3,6,7,1]),
    EightPuzzleState("START",0,[8,1,2,3,4,0,6,5,7]),
    EightPuzzleState("START",0,[1,0,6,5,8,2,4,3,7]),
    EightPuzzleState("START",0,[4,6,5,2,1,0,7,3,8]),
    EightPuzzleState("START",0,[2,0,6,3,4,5,7,8,1]),
    EightPuzzleState("START",0,[5,8,7,3,4,0,6,2,1]),
    EightPuzzleState("START",0,[3,7,6,5,4,1,2,0,8]),
    EightPuzzleState("START",0,[1,5,2,4,3,0,7,8,6]),
    EightPuzzleState("START",0,[3,2,1,5,7,8,4,0,6]),
    EightPuzzleState("START",0,[7,8,1,0,6,4,5,2,3]),
    EightPuzzleState("START",0,[3,0,5,4,8,1,2,7,6]),
    EightPuzzleState("START",0,[5,1,7,6,2,0,3,8,4]),
    EightPuzzleState("START",0,[5,1,3,0,2,4,7,6,8]),
    EightPuzzleState("START",0,[3,6,4,1,7,5,8,0,2]),
    EightPuzzleState("START",0,[1,5,8,0,2,6,4,7,3]),
    EightPuzzleState("START",0,[6,0,2,1,5,8,4,3,7]),
    EightPuzzleState("START",0,[1,2,4,0,8,3,7,6,5]),
    EightPuzzleState("START",0,[5,2,6,3,8,0,7,1,4]),
    EightPuzzleState("START",0,[1,0,6,7,3,5,2,8,4]),
    EightPuzzleState("START",0,[2,6,1,0,7,8,3,5,4])
    )

