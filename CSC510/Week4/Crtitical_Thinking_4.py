from simpleai.search import astar, SearchProblem
from simpleai.search.viewers import WebViewer
import random

WEIGHTS = [25, 35, 45]

GOAL = '''25-25-e-e
35-35-e-e
45-45-e-e'''

INITIAL = '''25-e-e-e
25-35-45-e
45-35-e-e'''



def list_to_string(list_):
    return '\n'.join(['-'.join(row) for row in list_])

def string_to_list(string_):
    return [row.split('-') for row in string_.split('\n')]

def generate_random():
    num_weight = random.randint(1,6)
    

class EigthPuzzleProblem(SearchProblem):
   
    def actions(self, state):
        '''Returns a list of potential moves given the current state.'''
        rungs = string_to_list(state)
        e_loc = []
        for rung in range(len(rungs)):
            for pos in range(len(rungs[0])):
                if rungs[rung][pos] == 'e' and (pos == 0 or (pos > 0 and rungs[rung][pos-1] != 'e')):
                    e_loc.append([rung, pos])

        actions = []
        for rung in range(len(rungs)):
            for pos in range(len(rungs[0])):
                if pos < len(rungs[0])-1 and rungs[rung][pos+1] == 'e' and rungs[rung][pos] != 'e':
                    for i in range(len(e_loc)):
                        if rung != e_loc[i][0]:
                            actions.append([[rung, pos],e_loc[i]])

        return actions

    def result(self, state, action):
        '''Return the resulting state after moving a piece to the empty space.
           (the "action" parameter contains the piece to move)
        '''
        rungs = string_to_list(state)
        n_rungs, e_rungs = action
        n_rung, n_pos = n_rungs
        e_rung, e_pos = e_rungs
        rungs[n_rung][n_pos], rungs[e_rung][e_pos] = rungs[e_rung][e_pos], rungs[n_rung][n_pos] 

        return list_to_string(rungs)

    def is_goal(self, state):
        '''Returns true if a state is the goal state.'''
        return state == GOAL 

    def cost(self, state1, action, state2):
        '''Returns the cost of performing an action. 
            The cost is the poundage of the weight.
        '''
        rungs = string_to_list(state1)
        n_rungs, e_rungs = action
        n_rung, n_pos = n_rungs
        return int(rungs[n_rung][n_pos])

    def heuristic(self, state):
        '''Returns an *estimation* of the distance from a state to the goal.
            Finds every weight that is in the wrong location and sums the weight. 
        '''
        rungs = string_to_list(state)
        goal = string_to_list(GOAL)
        cost = 0
        for rung_i in range(len(rungs)):
            for pos_i in range(len(rungs[rung_i])):
                if rungs[rung_i][pos_i] != goal[rung_i][pos_i] and rungs[rung_i][pos_i] != 'e':
                    cost += int(rungs[rung_i][pos_i])

        return cost



result = astar(EigthPuzzleProblem(INITIAL))
# if you want to use the visual debugger, use this instead:
# result = astar(EigthPuzzleProblem(INITIAL), viewer=WebViewer())

for action, state in result.path():
    print('Move number', action)
    print(state)

