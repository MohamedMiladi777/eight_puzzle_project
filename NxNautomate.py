import csv
import search
import random

from NxNpuzzle import NPuzzleState, NPuzzleSearchProblem, h1, h2, h3, h4, createRandomNPuzzle, isSolvable

heuristics = [h1, h2, h3, h4]

def createRandomSolvableNxNPuzzle(n, moves=100):
    while True:
        puzzle = createRandomNPuzzle(n, moves)
        if isSolvable(puzzle):
            return puzzle

def createRandomNxNPuzzle(n, moves=100):
    puzzle = NPuzzleState(n)
    for i in range(moves):
        puzzle = puzzle.result(random.choice(puzzle.legalMoves()))
    return puzzle

# Define the puzzle sizes
puzzle_sizes = [3, 4, 5]  # You can add more sizes as needed

# Open the results file and scenarios file
with open('resultsNxN.csv', 'w', newline='') as results_file, open('scenariosNxN.csv', 'w', newline='') as scenarios_file:
    results_writer = csv.writer(results_file)
    scenarios_writer = csv.writer(scenarios_file)

    # Write the header row
    results_writer.writerow(['Scenario', 'Heuristic', 'Depth', 'Expanded nodes', 'Fringe size'])

    # Initialize a dictionary to store the total depth, expanded nodes, and fringe size for each heuristic
    totals = {heuristic.__name__: {'depth': 0, 'expanded_nodes': 0, 'fringe_size': 0} for heuristic in heuristics}

    # Generate random scenarios for each puzzle size
    for size in puzzle_sizes:
        for _ in range(20):  # Generate 20 random scenarios for each size
            # Create a random NxN puzzle problem instance
            puzzle = createRandomNPuzzle(size, 50)  # Adjust the number of random moves as needed
            problem = NPuzzleSearchProblem(puzzle)

            # Get the initial state as a list
            initial_state = [cell for row in puzzle.cells for cell in row]

            # Write the scenario to the scenarios file
            scenarios_writer.writerow(initial_state)

            print(f"Scenario (Size {size}x{size}): {initial_state}")

            # For each heuristic
            for heuristic in heuristics:
                # Solve the problem using A* search with the heuristic
                actions = search.aStarSearch(problem, heuristic)

                # Record the results (depth, expanded nodes, fringe size)
                depth = len(actions)
                expanded_nodes = problem.expandedNodes
                fringe_size = problem.fringeSize

                # Add the results to the totals for this heuristic
                totals[heuristic.__name__]['depth'] += depth
                totals[heuristic.__name__]['expanded_nodes'] += expanded_nodes
                totals[heuristic.__name__]['fringe_size'] += fringe_size

                # Write the results to the CSV file
                results_writer.writerow([initial_state, heuristic.__name__, depth, expanded_nodes, fringe_size])

    # Calculate and print the average depth, expanded nodes, and fringe size for each heuristic
    print("\nAverage results for each heuristic:")
    for heuristic in heuristics:
        avg_depth = totals[heuristic.__name__]['depth'] / (20 * len(puzzle_sizes))
        avg_expanded_nodes = totals[heuristic.__name__]['expanded_nodes'] / (20 * len(puzzle_sizes))
        avg_fringe_size = totals[heuristic.__name__]['fringe_size'] / (20 * len(puzzle_sizes))

        print(f"{heuristic.__name__}: Depth {avg_depth}, Expanded nodes {avg_expanded_nodes}, Fringe size {avg_fringe_size}")

    # Decide on the best heuristic based on the averages
    best_heuristic = min(heuristics, key=lambda heuristic: totals[heuristic.__name__]['depth'])
    print(f"\nBest heuristic based on average depth: {best_heuristic.__name__}")
