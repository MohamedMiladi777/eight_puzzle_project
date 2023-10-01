import math
import search
import random
# class EightPuzzleState:
#
#     def __init__( self, numbers ):
#
#
#         self.cells = []
#
#         numbers = numbers[:] # Make a copy so as not to cause side-effects.
#
#         numbers.reverse()
#
#         for row in range( 3 ):
#
#             self.cells.append( [] )
#
#             for col in range( 3 ):
#
#                 if numbers:
#
#                     self.cells[row].append(numbers.pop())
#
#                 else:
#
#                     raise ValueError("Not enough numbers provided for the puzzle!")
#
#
#
#                 if self.cells[row][col] == 0:
#
#                     self.blankLocation = row, col

# class EightPuzzleState:
#     def __init__(self, numbers):
#         if len(numbers) != 9:
#             raise ValueError("Exactly 9 numbers must be provided for the puzzle!")
#
#         self.cells = []
#         numbers = numbers[:]  # Make a copy so as not to cause side-effects.
#
#         for row in range(3):
#             self.cells.append([])
#             for col in range(3):
#                 self.cells[row].append(numbers.pop(0))
#
#                 if self.cells[row][col] == 0:
#                     self.blankLocation = row, col
class EightPuzzleState:
    def __init__(self, numbers):
        if len(numbers) != 9:
            raise ValueError("Exactly 9 numbers must be provided for the puzzle!")

        self.cells = []
        numbers = numbers[:]  # Make a copy so as not to cause side-effects.

        for i in range(0, 9, 3):
            self.cells.append(numbers[i:i+3])

        # Find the location of the blank space (0)
        for row in range(3):
            for col in range(3):
                if self.cells[row][col] == 0:
                    self.blankLocation = row, col


 

    def isGoal( self ):

        """

          Checks to see if the puzzle is in its goal state.

            -------------

            |   | 1 | 2 |

            -------------

            | 3 | 4 | 5 |

            -------------

            | 6 | 7 | 8 |

            -------------



        >>> EightPuzzleState([0, 1, 2, 3, 4, 5, 6, 7, 8]).isGoal()

        True

 

        >>> EightPuzzleState([1, 0, 2, 3, 4, 5, 6, 7, 8]).isGoal()

        False

        """

        current = 0

        for row in range( 3 ):

            for col in range( 3 ):

                if current != self.cells[row][col]:

                    return False

                current += 1

        return True

 

    def legalMoves( self ):

        """

          Returns a list of legal moves from the current state.



        Moves consist of moving the blank space up, down, left or right.

        These are encoded as 'up', 'down', 'left' and 'right' respectively.

 

        >>> EightPuzzleState([0, 1, 2, 3, 4, 5, 6, 7, 8]).legalMoves()

        ['down', 'right']

        """

        moves = []

        row, col = self.blankLocation

        if(row != 0):

            moves.append('up')

        if(row != 2):

            moves.append('down')

        if(col != 0):

            moves.append('left')

        if(col != 2):

            moves.append('right')

        return moves



 

    def result(self, move):

        """

          Returns a new eightPuzzle with the current state and blankLocation

        updated based on the provided move.



        The move should be a string drawn from a list returned by legalMoves.

        Illegal moves will raise an exception, which may be an array bounds

        exception.



        NOTE: This function *does not* change the current object.  Instead,

        it returns a new object.

        """

        row, col = self.blankLocation

        if(move == 'up'):

            newrow = row - 1

            newcol = col

        elif(move == 'down'):

            newrow = row + 1

            newcol = col

        elif(move == 'left'):

            newrow = row

            newcol = col - 1

        elif(move == 'right'):

            newrow = row

            newcol = col + 1

        else:

            raise "Illegal Move"



        # Create a copy of the current eightPuzzle

        newPuzzle = EightPuzzleState([0, 0, 0, 0, 0, 0, 0, 0, 0])

        newPuzzle.cells = [values[:] for values in self.cells]

        # And update it to reflect the move

        newPuzzle.cells[row][col] = self.cells[newrow][newcol]

        newPuzzle.cells[newrow][newcol] = self.cells[row][col]

        newPuzzle.blankLocation = newrow, newcol



        return newPuzzle

    # def result(self, move):
    #     row, col = self.blankLocation
    #     if move == 'up':
    #         newrow = row - 1
    #         newcol = col
    #     elif move == 'down':
    #         newrow = row + 1
    #         newcol = col
    #     elif move == 'left':
    #         newrow = row
    #         newcol = col - 1
    #     elif move == 'right':
    #         newrow = row
    #         newcol = col + 1
    #     else:
    #         raise ValueError("Illegal Move")
    #
    #         # Create a copy of the current eightPuzzle
    #
    #     newPuzzle = EightPuzzleState([0, 0, 0, 0, 0, 0, 0, 0, 0])
    #
    #     newPuzzle.cells = [values[:] for values in self.cells]
    #
    #     # And update it to reflect the move
    #
    #     newPuzzle.cells[row][col] = self.cells[newrow][newcol]
    #
    #     newPuzzle.cells[newrow][newcol] = self.cells[row][col]
    #
    #     newPuzzle.blankLocation = newrow, newcol
    #
    #
    #
    #     return newPuzzle





    # Utilities for comparison and display

    def __eq__(self, other):

        """

            Overloads '==' such that two eightPuzzles with the same configuration

          are equal.

 

          >>> EightPuzzleState([0, 1, 2, 3, 4, 5, 6, 7, 8]) == \

              EightPuzzleState([1, 0, 2, 3, 4, 5, 6, 7, 8]).result('left')

          True

        """

        for row in range( 3 ):

            if self.cells[row] != other.cells[row]:

                return False

        return True

 

    def __hash__(self):

        return hash(str(self.cells))

 

    def __getAsciiString(self):

        """

          Returns a display string for the maze

        """

        lines = []

        horizontalLine = ('-' * (13))

        lines.append(horizontalLine)

        for row in self.cells:

            rowLine = '|'

            for col in row:

                if col == 0:

                    col = ' '

                rowLine = rowLine + ' ' + col.__str__() + ' |'

            lines.append(rowLine)

            lines.append(horizontalLine)

        return '\n'.join(lines)
    def __str__(self):

        return self.__getAsciiString()

# TODO: Implement The methods in this class

 

class EightPuzzleSearchProblem(search.SearchProblem):

 

    def __init__(self, puzzle):

        self.puzzle = puzzle

        self.expandedNodes = 0

        self.fringeSize = 0

 

    def getStartState(self):

        return self.puzzle

 

    def isGoalState(self, state):

        return state.isGoal()

 

    def getSuccessors(self, state):

        successors = []

        for move in state.legalMoves():

            successor = state.result(move)

            cost = 1  # Cost for all actions is 1

            successors.append((successor, move, cost))

 

            self.fringeSize +=1

        self.expandedNodes +=1

    

        return successors

 

    def getCostOfActions(self, actions):

        return len(actions)

 

 

EIGHT_PUZZLE_DATA = [[1, 0, 2, 3, 4, 5, 6, 7, 8],

                     [1, 7, 8, 2, 3, 4, 5, 6, 0],

                     [4, 3, 2, 7, 0, 5, 1, 6, 8],

                     [5, 1, 3, 4, 0, 2, 6, 7, 8],

                     [1, 2, 5, 7, 6, 8, 0, 4, 3],

                     [0, 3, 1, 6, 8, 2, 7, 5, 4]]

 

def loadEightPuzzle(puzzleNumber):

    """

      puzzleNumber: The number of the eight puzzle to load.

 

      Returns an eight puzzle object generated from one of the

      provided puzzles in EIGHT_PUZZLE_DATA.

 

      puzzleNumber can range from 0 to 5.

 

      >>> print loadEightPuzzle(0)

      -------------

      | 1 |   | 2 |

      -------------

      | 3 | 4 | 5 |

      -------------

      | 6 | 7 | 8 |

      -------------

    """

    return EightPuzzleState(EIGHT_PUZZLE_DATA[puzzleNumber])

def h1(state, problem=None):


    goal_state = EightPuzzleState([0, 1, 2, 3, 4, 5, 6, 7, 8])

    misplaced = 0

 

    for row in range(3):

        for col in range(3):

            if state.cells[row][col] != goal_state.cells[row][col]:

                misplaced += 1

 

    return misplaced

 

def h2(state, problem=None):

    goal_positions = {

        0: (0, 0), 1: (0, 1), 2: (0, 2),

        3: (1, 0), 4: (1, 1), 5: (1, 2),

        6: (2, 0), 7: (2, 1), 8: (2, 2),

    }

 

    total_distance = 0

 

    # Iterate through the current state's cells

    for row in range(3):

        for col in range(3):

            tile = state.cells[row][col]

            if tile != 0:  # Skip the blank tile (0)

                # Find the goal position of the current tile

                goal_row, goal_col = goal_positions[tile]

                # Calculate the Euclidean distance and add it to the total

                distance = math.sqrt((row - goal_row) ** 2 + (col - goal_col) ** 2)

                total_distance += distance

    

    return total_distance

 

 

def h3(state, problem=None):

    goal_positions = {

        0: (0, 0), 1: (0, 1), 2: (0, 2),

        3: (1, 0), 4: (1, 1), 5: (1, 2),

        6: (2, 0), 7: (2, 1), 8: (2, 2),

    }

 

    total_distance = 0

 

    # Iterate through the current state's cells

    for row in range(3):

        for col in range(3):

            tile = state.cells[row][col]

            if tile != 0:  # Skip the blank tile (0)

                # Find the goal position of the current tile

                goal_row, goal_col = goal_positions[tile]

                # Calculate the Manhattan distance and add it to the total

                distance = abs(row - goal_row) + abs(col - goal_col)

                total_distance += distance

 

    return total_distance

 

# ... (rest of the code)

 

def h4(state, problem=None):


    goal_positions = {

        0: (0, 0), 1: (0, 1), 2: (0, 2),

        3: (1, 0), 4: (1, 1), 5: (1, 2),

        6: (2, 0), 7: (2, 1), 8: (2, 2),

    }

 

    out_of_row_count = 0

    out_of_column_count = 0

 

    # Iterate through the current state's cells

    for row in range(3):

        for col in range(3):

            tile = state.cells[row][col]

            if tile != 0:  # Skip the blank tile (0)

                # Find the goal position of the current tile

                goal_row, goal_col = goal_positions[tile]

                # Check if the tile is out of row or column

                if row != goal_row:

                    out_of_row_count += 1

                if col != goal_col:

                    out_of_column_count += 1

 

    return out_of_row_count + out_of_column_count

 

# ... (rest of the code)

 

 

def createRandomEightPuzzle(moves=100):


    puzzle = EightPuzzleState([0,1,2,3,4,5,6,7,8])

    for i in range(moves):

        # Execute a random legal move

        puzzle = puzzle.result(random.sample(puzzle.legalMoves(), 1)[0])

    return puzzle

 

if __name__ == '__main__':

    puzzle = createRandomEightPuzzle(25)

    print('A random puzzle:')

    print(puzzle)


    problem = EightPuzzleSearchProblem(puzzle)

    path = search.aStarSearch(problem, heuristic = h2)

    print('A* found a path of %d moves: %s' % (len(path), str(path)))

    curr = puzzle

    i = 1

    for a in path:

        curr = curr.result(a)

        print('After %d move%s: %s' % (i, ("", "s")[i>1], a))

        print(curr)

 

        #input("Press return for the next state...")   # wait for key stroke

        i += 1