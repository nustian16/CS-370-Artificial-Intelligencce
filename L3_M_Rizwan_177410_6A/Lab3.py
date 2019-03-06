import sys
from simpleai.search import SearchProblem, breadth_first, depth_first,limited_depth_first, iterative_limited_depth_first, uniform_cost

'''
8 puzzle problem, a smaller version of the fifteen puzzle:
http://en.wikipedia.org/wiki/Fifteen_puzzle
States are defined as string representations of the pieces on the puzzle.
Actions denote what piece will be moved to the empty space.
States must allways be inmutable. We will use strings, but internally most of
the time we will convert those strings to lists, which are easier to handle.
For example, the state (string):
'1-2-3
 4-5-6
 7-8-e'
will become (in lists):
[['1', '2', '3'],
 ['4', '5', '6'],
 ['7', '8', 'e']]
'''
from timeit import default_timer as timer
from simpleai.search import * 
'''
SearchProblem, breadth_first, depth_first, limited_depth_first, iterative_limited_depth_first, uniform_cost'''

GOAL = '''Bucharest'''
INITIAL = '''Arad'''
graph = {"Oradea": {
                "Zerind": 71,
                "Timisoara": 118
            }
 ,"Arad": {
                "Sibiu": 140,
                "Timisoara": 118,
                "Zerind":75
            }
 ,"Zerind": {
                "Oradea": 70,
                "Arad": 75
            }
 ,"Sibiu": {
                "Arad": 140,
                "Oradea": 151,
                "Fagaras":99,
                "Rimnicu Vilcea":80
            }
 ,"Fagaras": {
                "Sibiu": 99,
                "Bucharest": 211
            }
 ,"Rimnicu Vilcea": {
                "Sibiu": 80,
                "Pitesti": 97,
                "Craiova":146
            }
 ,"Timisoara": {
                "Arad": 118,
                "Lugoj": 111
                }
  ,"Lugoj": {
                "Timisoara": 111,
                "Mehadia": 70
                }
 ,"Mehadia": {
                "Lugoj": 70,
                "Drobeta": 74
                }
 ,"Drobeta": {
                "Mehadia": 75,
                "Craiova": 120
                }
  ,"Craiova": {
                "Drobeta": 120,
                "Rimnicu Vilcea": 146,
                "Pitesti": 138
                }
 ,"Pitesti": {
                "Craiova": 138,
                "Rimnicu Vilcea": 97,
                "Bucharest": 101
                }
 ,"Bucharest": {
                "Pitesti": 101,
                "Fagaras": 211
                }
}
class EigthPuzzleProblem(SearchProblem):
    def actions(self, state):
        '''Returns a list of the pieces we can move to the empty space.'''
        return graph[state].keys()

    def result(self, state, action):
        '''Return the resulting state after moving a piece to the empty space.
           (the "action" parameter contains the piece to move)
        '''
        return action

    def is_goal(self, state):
        '''Returns true if a state is the goal state.'''
        return str(state) == str(GOAL)

    def cost(self, state1, action, state2):
        '''Uniform cost
        '''
        return int(graph[state1][action])

start = timer()
#result = breadth_first(EigthPuzzleProblem(INITIAL), graph_search=True)
#result = uniform_cost(EigthPuzzleProblem(INITIAL), graph_search=True)
#result = limited_depth_first(EigthPuzzleProblem(INITIAL),30,graph_search=True)
#result = limited_depth_first(EigthPuzzleProblem(INITIAL),50,graph_search=True)
#result = limited_depth_first(EigthPuzzleProblem(INITIAL),100,graph_search=True)
result = iterative_limited_depth_first(EigthPuzzleProblem(INITIAL),graph_search=True) #intial is declared above as Arad
end = timer()

# Time
print "Time: " + str(end - start)

# cost of solution
print result.cost

# Solution
for action, state in result.path():
    print 'Move number', action
    print state
