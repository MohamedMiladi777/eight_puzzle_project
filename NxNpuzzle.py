import math
import search
import random

class NPuzzleState:

    def __init__(self, numbers, n):
        if len(numbers) != n * n:
            raise ValueError("Exactly {} numbers must be provided for the puzzle!".format(n * n))

        self.cells = []
        self.n = n

        numbers = numbers[:]  # Make a copy so as not to cause side-effects.
        numbers.reverse()

        for row in range(n):
            self.cells.append([])
            for col in range(n):
                if numbers:
                    self.cells[row].append(numbers.pop())
                else:
                    raise ValueError("Not enough numbers provided for the puzzle!")

                if self.cells[row][col] == 0:
                    self.blankLocation = row, col

    def isGoal(self):
        current = 0
        for row in range(self.n):
            for col in range(self.n):
                if current != self.cells[row][col]:
                    return False
                current += 1
        return True

    def legalMoves(self):
        moves = []
        row, col = self.blankLocation

        if row != 0:
            moves.append('up')
        if row != self.n - 1:
            moves.append('down')
        if col != 0:
            moves.append('left')
        if col != self.n - 1:
            moves.append('right')

        return moves

    def result(self, move):
        row, col = self.blankLocation

        if move == 'up':
            newrow = row - 1
            newcol = col
        elif move == 'down':
            newrow = row + 1
            newcol = col
        elif move == 'left':
            newrow = row
            newcol = col - 1
        elif move == 'right':
            newrow = row
            newcol = col + 1
        else:
            raise ValueError("Illegal Move")

        newPuzzle = NPuzzleState([0] * (self.n * self.n), self.n)
        newPuzzle.cells = [values[:] for values in self.cells]
        newPuzzle.cells[row][col] = self.cells[newrow][newcol]
        newPuzzle.cells[newrow][newcol] = self.cells[row][col]
        newPuzzle.blankLocation = newrow, newcol

        return newPuzzle

    def __eq__(self, other):
        for row in range(self.n):
            if self.cells[row] != other.cells[row]:
                return False
        return True

    def __hash__(self):
        return hash(str(self.cells))

    def __getAsciiString(self):
        lines = []
        horizontalLine = '-' * (4 * self.n + 1)
        lines.append(horizontalLine)
        for row in self.cells:
            rowLine = '|'
            for col in row:
                if col == 0:
                    col = ' '
                rowLine = rowLine + ' ' + str(col) + ' |'
            lines.append(rowLine)
            lines.append(horizontalLine)
        return '\n'.join(lines)

    def __str__(self):
        return self.__getAsciiString()

class NPuzzleSearchProblem(search.SearchProblem):

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
            self.fringeSize += 1
        self.expandedNodes += 1
        return successors

    def getCostOfActions(self, actions):
        return len(actions)

def h1(state, problem=None):
    goal_state = NPuzzleState(list(range(state.n ** 2)), state.n)
    misplaced = 0

    for row in range(state.n):
        for col in range(state.n):
            if state.cells[row][col] != goal_state.cells[row][col]:
                misplaced += 1

    return misplaced

def h2(state, problem=None):
    goal_positions = {}
    for i in range(state.n ** 2):
        goal_positions[i] = divmod(i, state.n)

    total_distance = 0

    for row in range(state.n):
        for col in range(state.n):
            tile = state.cells[row][col]
            if tile != 0:
                goal_row, goal_col = goal_positions[tile]
                distance = math.sqrt((row - goal_row) ** 2 + (col - goal_col) ** 2)
                total_distance += distance

    return total_distance

def h3(state, problem=None):
    goal_positions = {}
    for i in range(state.n ** 2):
        goal_positions[i] = divmod(i, state.n)

    total_distance = 0

    for row in range(state.n):
        for col in range(state.n):
            tile = state.cells[row][col]
            if tile != 0:
                goal_row, goal_col = goal_positions[tile]
                distance = abs(row - goal_row) + abs(col - goal_col)
                total_distance += distance

    return total_distance

def h4(state, problem=None):
    goal_positions = {}
    for i in range(state.n ** 2):
        goal_positions[i] = divmod(i, state.n)

    out_of_row_count = 0
    out_of_column_count = 0

    for row in range(state.n):
        for col in range(state.n):
            tile = state.cells[row][col]
            if tile != 0:
                goal_row, goal_col = goal_positions[tile]
                if row != goal_row:
                    out_of_row_count += 1
                if col != goal_col:
                    out_of_column_count += 1

    return out_of_row_count + out_of_column_count

def createRandomNPuzzle(n, moves=100):
    puzzle = NPuzzleState(list(range(n ** 2)), n)
    for i in range(moves):
        puzzle = puzzle.result(random.sample(puzzle.legalMoves(), 1)[0])
    return puzzle

if __name__ == '__main__':
    n = 5  # Change this to the desired NxN puzzle size
    puzzle = createRandomNPuzzle(n, 50)  # Adjust the number of random moves as needed
    print('A random {}x{} puzzle:'.format(n, n))
    print(puzzle)

    problem = NPuzzleSearchProblem(puzzle)
    path = search.aStarSearch(problem, heuristic=h2)
    print('A* found a path of {} moves: {}'.format(len(path), str(path)))

    curr = puzzle
    i = 1
    for a in path:
        curr = curr.result(a)
        print('After {} move{}:'.format(i, ("", "s")[i > 1]))
        print(curr)
        i += 1
