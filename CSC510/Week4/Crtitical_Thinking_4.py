from simpleai.search import astar, SearchProblem
from simpleai.search.viewers import WebViewer



"""
Moving weights on a weight lifiting rack
each weight has a cost of the weights size
what is the cheapest way to move the weights to be in order
"""


GOAL = '''25-25-e
          35-35-e
          45-45-e'''

INITIAL = '''25-45-e
             25-35-e
             35-45-e'''



def list_to_string(list_):
    return '\n'.join(['-'.join(row) for row in list_])


def string_to_list(string_):
    return [row.split('-') for row in string_.split('\n')]


def find_location(rows, element_to_find):
    '''Find the location of a piece in the puzzle.
       Returns a tuple: row, column'''
    for ir, row in enumerate(rows):
        for ic, element in enumerate(row):
            if element == element_to_find:
                return ir, ic


# we create a cache for the goal position of each piece, so we don't have to
# recalculate them every time
goal_positions = {}
rows_goal = string_to_list(GOAL)
for number in '12345678e':
    goal_positions[number] = find_location(rows_goal, number)



class EigthPuzzleProblem(SearchProblem):
   
    def actions(self, state):
        '''Returns a list of the pieces we can move to the empty space.'''
        rows = string_to_list(state)
        row_e, col_e = find_location(rows, 'e')

        actions = []
        

        return actions

    def result(self, state, action):
        '''Return the resulting state after moving a piece to the empty space.
           (the "action" parameter contains the piece to move)
        '''
     
        return list_to_string(tab)

    def is_goal(self, state):
        '''Returns true if a state is the goal state.'''
        print(self.note_number)
        return state == GOAL or self.note_number == len(midi_sequence)-1

    def cost(self, state1, action, state2):
        '''Returns the cost of performing an action. No useful on this problem, i
           but needed.
        '''
        print()
        return 1

    def heuristic(self, state):
        '''Returns an *estimation* of the distance from a state to the goal.
           We are using the manhattan distance.
        '''
        

        return 0


result = astar(EigthPuzzleProblem(INITIAL))
# if you want to use the visual debugger, use this instead:
# result = astar(EigthPuzzleProblem(INITIAL), viewer=WebViewer())

for action, state in result.path():
    print('Move number', action)
    print(state)
