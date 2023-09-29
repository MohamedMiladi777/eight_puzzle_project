import csv
import time
from eightpuzzle import EightPuzzleSearchProblem, h1, h2, h3, h4, createRandomEightPuzzle
from search import aStarSearch

# Define the heuristics in a list
heuristics = [h1, h2, h3, h4]

# Define the number of puzzles to generate
num_puzzles = 100

# Open the CSV file for writing
with open('scenarios.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(["Heuristic", "Depth", "Expanded Nodes", "Fringe Size", "Time"])

    # Generate and solve puzzles
    for i in range(num_puzzles):
        puzzle = createRandomEightPuzzle(25)
        problem = EightPuzzleSearchProblem(puzzle)

        for heuristic in heuristics:
            start_time = time.time()
            solution = aStarSearch(problem, heuristic)
            end_time = time.time()

            depth = len(solution)
            expanded_nodes = problem.expandedNodes
            fringe_size = problem.fringeSize
            elapsed_time = end_time - start_time

            # Write the results for this puzzle and heuristic
            writer.writerow([heuristic.__name__, depth, expanded_nodes, fringe_size, elapsed_time])
