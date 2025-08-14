from simpleai.search import astar, SearchProblem
from simpleai.search.viewers import WebViewer

GOAL = '''25-25-e-e
35-35-e-e
45-45-e-e'''

INITIAL_1 = '''25-e-e-e
25-35-45-e
45-35-e-e'''

INITIAL_2 = '''45-35-e-e
45-e-e-e
25-35-25-e'''

INITIAL_3 = '''35-25-45-e
e-e-e-e
25-35-45-e'''

INITIAL_LIST = [INITIAL_1, INITIAL_2, INITIAL_3]


def list_to_string(list_):
    return '\n'.join(['-'.join(row) for row in list_])

def string_to_list(string_):
    return [row.split('-') for row in string_.split('\n')]

    
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

###### User Interface ######
initial = ""
while(True):
    print("Would you like to use a precoded initial state (p) or create a custom state? (c)")
    answer = input("(p) or (c)?: ")
    if answer == 'p':
        print("please choose from the precoded initial states")
        print("Option 1\n" + INITIAL_1 + "\n")
        print("Option 2\n" + INITIAL_2 + "\n")
        print("Option 3\n" + INITIAL_3 + "\n")
        while(True):
            choice = input("Please type the number for the desired option: ")
            choice = int(choice)
            if choice <= len(INITIAL_LIST) and choice > 0:
                initial = INITIAL_LIST[choice - 1]
                break
            print("ERROR: Please enter \'1\', \'2\' or \'3\'")
        break
    elif answer == 'c':
        while(True):
            print("please enter an initial state where you have (2) 25 pound weights, (2) 35 pound weights and (2) 45 pound weights. Put a space between each weight (e.g. 25 35 35)")
            rung_1 = input("Enter the order of weights on the first rung: ")
            rung_2 = input("Enter the order of weights on the second rung: ")
            rung_3 = input("Enter the order of weights on the third rung: ")

            rung_1 = rung_1.split()
            rung_2 = rung_2.split()
            rung_3 = rung_3.split()

            if (len(rung_1) + len(rung_2) + len(rung_3)) == 6:
                def fill_with_e(rung):
                    while(len(rung)<4):
                        rung.append('e')
                    return rung
                fill_with_e(rung_1)
                fill_with_e(rung_2)
                fill_with_e(rung_3)

                initial_list = []
                initial_list.append(rung_1)
                initial_list.append(rung_2)
                initial_list.append(rung_3)
                initial = list_to_string(initial_list)
                break
            print("ERROR: Please enter exactly 6 weights where (2) are 25, (2) are 35 and (2) are 45")
        break

    else:
        print("ERROR: Please enter \'p\' or \'c\'")

result = astar(EigthPuzzleProblem(initial))

count = 0
for action, state in result.path():
    print('Move number ' + str(count))
    count+=1
    print(state)
    print()

