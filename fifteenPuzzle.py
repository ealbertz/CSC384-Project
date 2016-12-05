
'''Statespace 15-Puzzle
'''
from search import *

class FifteenPuzzleState(StateSpace):
    StateSpace.n=0

    def __init__(self, action, gval, state, parent = None):
        '''Create an puzzle stae object. The  input parameter state represents the puzzle as a list of numbers in teh range[0-15],
        where zero represents the blank tile.
        '''

        StateSpace.__init__(self, action,gval,parent)
        self.state=state

        #The goal state is set to when the tiles are in numerical order
        self.goal_state=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]

    def successors(self):
        '''
        Generates all actions that can be performed from this state, and the states those actions will create. 
        '''
        successors=[]
        transition_cost =1
        position_blank=self.state.index(0)

        if position_blank < 12: #possible to slide blank tile down
            state = self.state[:]
            state[position_blank] = state[position_blank + 4]
            state[position_blank + 4] = 0 
            new_state = FifteenPuzzleState("Blank down", self.gval+transition_cost, state, self)
            successors.append(new_state)
        if position_blank > 2: #possible to slide blank tile up
            state = self.state[:]
            state[position_blank] = state[position_blank - 4]
            state[position_blank - 4] = 0 
            new_state = FifteenPuzzleState("Blank up", self.gval+transition_cost, state, self)
            successors.append(new_state)

        if position_blank % 4 < 3: #possible to slide blank tile right
            state = self.state[:]
            state[position_blank] = state[position_blank + 1]
            state[position_blank + 1] = 0 
            new_state = FifteenPuzzleState("Blank right", self.gval+transition_cost, state, self)
            successors.append(new_state)

        if position_blank % 4 > 0: #possible to slide blank tile left
            state = self.state[:]
            state[position_blank] = state[position_blank - 1]
            state[position_blank - 1] = 0 
            new_state = FifteenPuzzleState("Blank left", self.gval+transition_cost, state, self)
            successors.append(new_state)

        return successors



    def hashable_state(self):
        return tuple(self.state)


    def print_state(self):
        if self.parent:
            print("Action= \"{}\", S{}, g-value = {}, (From State{})".format(self.action, self.index, self.gval, self.parent.index))
            print_state_picture(self)
        else:
            print("Action= \"{}\", S{}, g-value = {}, (Initial State)".format(self.action, self.index, self.gval))
            print_state_picture(self)


    def print_state_picture(self):

        print("|-------------------|")
        print("| {} | {} | {} | {} |".format(self.state[0],self.state[1],self.state[2]),self.state[3])
        print("|-------------------|")
        print("| {} | {} | {} | {} |".format(self.state[4],self.state[5],self.state[6]), self.state[7])
        print("|-------------------|")
        print("| {} | {} | {} | {} |".format(self.state[8],self.state[9],self.state[10], self.state[11]))
        print("|-------------------|")
        print("| {} | {} | {} | {} |".format(self.state[12],self.state[13],self.state[14], self.state[15]))
        print("|-------------------|")




def fifteenPuzzle_goal_state(state):
    '''Returns true if we have reached a goal state'''
    '''Input: an fifteenPuzzle state'''
    '''Output: True (if goal) or False (if not)'''
    return(FifteenPuzzleState.goal_state == state.state)





