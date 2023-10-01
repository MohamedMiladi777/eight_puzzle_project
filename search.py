
import util

import heapq

# def astar_search(problem, heuristic=None):
#     """
#     A* search algorithm.
#
#     Args:
#         problem: An instance of a search problem.
#         heuristic: A heuristic function that estimates the cost to reach the goal from a given state (optional).
#
#     Returns:
#         A list of actions that lead to the goal state, or None if no solution is found.
#     """
#     frontier = [(problem.getStartState(), [], 0)]  # Priority queue: (state, actions, cost)
#     explored = set()
#
#     while frontier:
#         state, actions, cost = frontier.pop(0)
#
#         if state in explored:
#             continue
#
#         if problem.isGoalState(state):
#             return actions
#
#         explored.add(state)
#
#         for successor, action, step_cost in problem.getSuccessors(state):
#             if successor not in explored:
#                 priority = cost + step_cost
#                 if heuristic:
#                     priority += heuristic(successor, problem)
#                 frontier.append((successor, actions + [action], cost + step_cost))
#                 frontier.sort(key=lambda x: x[2] + heuristic(x[0], problem))
#
#     return None  # No solution found
# def astar_search(problem, heuristic=None):
#     frontier = util.PriorityQueue()
#     explored = set()
#
#     start_state = problem.getStartState()
#     start_node = (start_state, [], 0)
#
#     frontier.push(start_node, 0)
#
#     while not frontier.isEmpty():
#         state, actions, cost = frontier.pop()
#
#         if state in explored:
#             continue
#
#         if problem.isGoalState(state):
#             return actions
#
#         explored.add(state)
#
#         for successor, action, step_cost in problem.getSuccessors(state):
#             if successor not in explored:
#                 new_cost = cost + step_cost
#                 if heuristic:
#                     priority = new_cost + heuristic(successor, problem)
#                 else:
#                     priority = new_cost
#                 frontier.push((successor, actions + [action], new_cost), priority)
#
#     return None
def astar_search(problem, heuristic=None):
    frontier = util.PriorityQueue()
    explored = set()

    start_state = problem.getStartState()
    start_node = (start_state, [], 0)

    frontier.push(start_node, 0)

    while not frontier.isEmpty():
        state, actions, cost = frontier.pop()

        if problem.isGoalState(state):
            return actions

        if state not in explored:
            explored.add(state)

            for successor, action, step_cost in problem.getSuccessors(state):
                new_cost = cost + step_cost
                if successor not in explored:
                    if heuristic:
                        priority = new_cost + heuristic(successor, problem)
                    else:
                        priority = new_cost
                    frontier.push((successor, actions + [action], new_cost), priority)



# Example usage:
# path = astar_search(problem, heuristic=h1)

class SearchProblem:

    def getStartState(self):

        util.raiseNotDefined()

    def isGoalState(self, state):

        util.raiseNotDefined()



    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):

        util.raiseNotDefined()


def tinyMazeSearch(problem):
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

# def depthFirstSearch(problem):
#
#     #states to be explored (LIFO). holds nodes in form (state, action)
#     frontier = util.Stack()
#     #previously explored states (for path checking), holds states
#     exploredNodes = []
#     #define start node
#     startState = problem.getStartState()
#     startNode = (startState, [])
#
#     frontier.push(startNode)
#
#     while not frontier.isEmpty():
#         #begin exploring last (most-recently-pushed) node on frontier
#         currentState, actions = frontier.pop()
#
#         if currentState not in exploredNodes:
#             #mark current node as explored
#             exploredNodes.append(currentState)
################Debugging, DFS TOO SLOW################
def depthFirstSearch(problem):
    #states to be explored (LIFO). holds nodes in form (state, action)
    frontier = util.Stack()
    #previously explored states (for path checking), holds states
    exploredNodes = set()  # Change this line
    #define start node
    startState = problem.getStartState()
    startNode = (startState, [])

    frontier.push(startNode)

    while not frontier.isEmpty():
    #begin exploring last (most-recently-pushed) node on frontier
        currentState, actions = frontier.pop()

        if currentState not in exploredNodes:
        #mark current node as explored
                            exploredNodes.add(currentState)  # And this line

        if problem.isGoalState(currentState):
            return actions
        else:
                #get list of possible successor nodes in 
                #form (successor, action, stepCost)
                successors = problem.getSuccessors(currentState)
                
                #push each successor to frontier
                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    newNode = (succState, newAction)
                    frontier.push(newNode)

    return actions  

# def breadthFirstSearch(problem):
#
#     #to be explored (FIFO)
#     frontier = util.Queue()
#
#     #previously expanded states (for cycle checking), holds states
#     exploredNodes = []
#
#     startState = problem.getStartState()
#     startNode = (startState, [], 0) #(state, action, cost)
#
#     frontier.push(startNode)
#
#     while not frontier.isEmpty():
#         #begin exploring first (earliest-pushed) node on frontier
#         currentState, actions, currentCost = frontier.pop()
#
#         if currentState not in exploredNodes:
#             #put popped node state into explored list
#             exploredNodes.append(currentState)
#Debugging, BFS TOO SLOW
def breadthFirstSearch(problem):
    frontier = util.Queue()

    #previously expanded states (for cycle checking), holds states
    exploredNodes = set()  # Change this line

    startState = problem.getStartState()
    startNode = (startState, [], 0) #(state, action, cost)

    frontier.push(startNode)

    while not frontier.isEmpty():
        #begin exploring first (earliest-pushed) node on frontier
        currentState, actions, currentCost = frontier.pop()

        if currentState not in exploredNodes:
            #put popped node state into explored list
            exploredNodes.add(currentState)  # And this line

            # ... rest of your code ...

            if problem.isGoalState(currentState):
                return actions
            else:
                #list of (successor, action, stepCost)
                successors = problem.getSuccessors(currentState)
                
                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    newCost = currentCost + succCost
                    newNode = (succState, newAction, newCost)

                    frontier.push(newNode)

    return actions
        
def uniformCostSearch(problem):
    #to be explored (FIFO): holds (item, cost)
    frontier = util.PriorityQueue()

    #previously expanded states (for cycle checking), holds state:cost
    exploredNodes = {}
    
    startState = problem.getStartState()
    startNode = (startState, [], 0) #(state, action, cost)
    
    frontier.push(startNode, 0)
    
    while not frontier.isEmpty():
        #begin exploring first (lowest-cost) node on frontier
        currentState, actions, currentCost = frontier.pop()
       
        if (currentState not in exploredNodes) or (currentCost < exploredNodes[currentState]):
            #put popped node's state into explored list
            exploredNodes[currentState] = currentCost

            if problem.isGoalState(currentState):
                return actions
            else:
                #list of (successor, action, stepCost)
                successors = problem.getSuccessors(currentState)
                
                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    newCost = currentCost + succCost
                    newNode = (succState, newAction, newCost)

                    frontier.update(newNode, newCost)

    return actions

def nullHeuristic(state, problem=None):

    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    #to be explored (FIFO): takes in item, cost+heuristic
    frontier = util.PriorityQueue()

    exploredNodes = [] #holds (state, cost)

    startState = problem.getStartState()
    startNode = (startState, [], 0) #(state, action, cost)

    frontier.push(startNode, 0)

    while not frontier.isEmpty():

        #begin exploring first (lowest-combined (cost+heuristic) ) node on frontier
        currentState, actions, currentCost = frontier.pop()

        #put popped node into explored list
        currentNode = (currentState, currentCost)
        exploredNodes.append((currentState, currentCost))

        if problem.isGoalState(currentState):
            return actions

        else:
            #list of (successor, action, stepCost)
            successors = problem.getSuccessors(currentState)

            #examine each successor
            for succState, succAction, succCost in successors:
                newAction = actions + [succAction]
                newCost = problem.getCostOfActions(newAction)
                newNode = (succState, newAction, newCost)

                #check if this successor has been explored
                already_explored = False
                for explored in exploredNodes:
                    #examine each explored node tuple
                    exploredState, exploredCost = explored

                    if (succState == exploredState) and (newCost >= exploredCost):
                        already_explored = True

                #if this successor not explored, put on frontier and explored list
                if not already_explored:
                    frontier.push(newNode, newCost + heuristic(succState, problem))
                    exploredNodes.append((succState, newCost))

    return actions


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch