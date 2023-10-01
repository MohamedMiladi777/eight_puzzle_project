# import csv
# import time
# from eightpuzzle import EightPuzzleSearchProblem, h1, h2, h3, h4, createRandomEightPuzzle
# from search import aStarSearch
#
# # Define the heuristics in a list
# heuristics = [h1, h2, h3, h4]
#
# # Define the number of puzzles to generate
# num_puzzles = 100
#
# # Open the CSV file for writing
# with open('scenarios.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     # Write the header row
#     writer.writerow(["Heuristic", "Depth", "Expanded Nodes", "Fringe Size", "Time"])
#
#     # Generate and solve puzzles
#     for i in range(num_puzzles):
#         puzzle = createRandomEightPuzzle(25)
#         problem = EightPuzzleSearchProblem(puzzle)
#
#         for heuristic in heuristics:
#             start_time = time.time()
#             solution = aStarSearch(problem, heuristic)
#             end_time = time.time()
#
#             depth = len(solution)
#             expanded_nodes = problem.expandedNodes
#             fringe_size = problem.fringeSize
#             elapsed_time = end_time - start_time
#
#             # Write the results for this puzzle and heuristic
#             writer.writerow([heuristic.__name__, depth, expanded_nodes, fringe_size, elapsed_time])

# import csv
# import eightpuzzle as ep
# import search
#
# # Define the heuristics
# heuristics = [ep.h1, ep.h2, ep.h3, ep.h4]
#
# # Define a function to run a scenario and record the results
# def run_scenario(puzzle, heuristic):
#     problem = ep.EightPuzzleSearchProblem(puzzle)
#     actions = search.aStarSearch(problem, heuristic)
#     return len(actions), problem.expandedNodes, problem.fringeSize
#
# # Open the scenarios file
# with open('scenarios.csv', 'r') as f:
#     reader = csv.reader(f)
#     scenarios = list(reader)
#
# # Open the results file
# with open('results.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Scenario', 'Heuristic', 'Depth', 'ExpandedNodes', 'FringeSize'])
#
#     # For each scenario...
#     for scenario in scenarios:
#         # Generate the puzzle
#         #puzzle = ep.EightPuzzleState(list(map(int, scenario)))
#         print(scenario)
#         puzzle = ep.EightPuzzleState([int(num) for num in scenario])
#
#
#         # For each heuristic...
#         for i, heuristic in enumerate(heuristics):
#             # Run the scenario and record the results
#             depth, expanded_nodes, fringe_size = run_scenario(puzzle, heuristic)
#             writer.writerow([scenario, f'h{i+1}', depth, expanded_nodes, fringe_size])



###############Works perfectly#####################
# import csv
# import eightpuzzle as ep
# import search
#
# # Define the heuristics
# heuristics = [ep.h1, ep.h2, ep.h3, ep.h4]
#
# # Open the scenarios file
# with open('scenarios.csv', 'r') as scenarios_file:
#     scenarios = csv.reader(scenarios_file)
#
#     # Open the results file
#     with open('results.csv', 'w', newline='') as results_file:
#         results_writer = csv.writer(results_file)
#
#         # Write the header row
#         results_writer.writerow(['Scenario', 'Heuristic', 'Depth', 'Expanded nodes', 'Fringe size'])
#
#         # For each scenario
#         for scenario in scenarios:
#             # Parse the scenario to get the initial state
#
#             initial_state = list(map(int, scenario))
#             print(f"Scenario: {initial_state}")  # Add this line
#
#             # Create an 8-puzzle problem instance
#             puzzle = ep.EightPuzzleState(initial_state)
#             problem = ep.EightPuzzleSearchProblem(puzzle)
#
#             # For each heuristic
#             for heuristic in heuristics:
#                 # Solve the problem using A* search with the heuristic
#                 actions = search.aStarSearch(problem, heuristic)
#
#                 # Record the results (depth, expanded nodes, fringe size)
#                 depth = len(actions)
#                 expanded_nodes = problem.expandedNodes
#                 fringe_size = problem.fringeSize
#
#                 # Write the results to the CSV file
#                 results_writer.writerow([initial_state, heuristic.__name__, depth, expanded_nodes, fringe_size])
######################################################







# import csv
# import eightpuzzle as ep
# import search
#
# # Define the heuristics
# heuristics = [ep.h1, ep.h2, ep.h3, ep.h4]
#
# # Open the scenarios file
# with open('scenarios.csv', 'r') as scenarios_file:
#     scenarios = csv.reader(scenarios_file)
#
#     # Open the results file
#     with open('results.csv', 'w', newline='') as results_file:
#         results_writer = csv.writer(results_file)
#
#         # Write the header row
#         results_writer.writerow(['Scenario', 'Heuristic', 'Depth', 'Expanded nodes', 'Fringe size'])
#
#         # For each scenario
#         for scenario in scenarios:
#             if scenario:  # Skip empty lines
#                 # Parse the scenario to get the initial state
#                 initial_state = list(map(int, scenario))
#                 print(f"Scenario: {initial_state}")  # Add this line
#
#                 # Create an 8-puzzle problem instance
#                 puzzle = ep.EightPuzzleState(initial_state)
#                 problem = ep.EightPuzzleSearchProblem(puzzle)
#
#                 # For each heuristic
#                 for heuristic in heuristics:
#                     # Solve the problem using A* search with the heuristic
#                     actions = search.aStarSearch(problem, heuristic)
#
#                     # Record the results (depth, expanded nodes, fringe size)
#                     depth = len(actions)
#                     expanded_nodes = problem.expandedNodes
#                     fringe_size = problem.fringeSize
#
#                     # Write the results to the CSV file
#                     results_writer.writerow([initial_state, heuristic.__name__, depth, expanded_nodes, fringe_size])
#
#
#
#

# import csv
# import eightpuzzle as ep
# import search
# import random
#
# # Define the heuristics
# heuristics = [ep.h1, ep.h2, ep.h3, ep.h4]
#
# def createRandomEightPuzzle(moves=100):
#     puzzle = ep.EightPuzzleState([0,1,2,3,4,5,6,7,8])
#     for i in range(moves):
#         puzzle = puzzle.result(random.choice(puzzle.legalMoves()))
#     return puzzle
#
# # Open the results file and scenarios file
# with open('results.csv', 'w', newline='') as results_file, open('scenarios.csv', 'w', newline='') as scenarios_file:
#     results_writer = csv.writer(results_file)
#     scenarios_writer = csv.writer(scenarios_file)
#
#     # Write the header row
#     results_writer.writerow(['Scenario', 'Heuristic', 'Depth', 'Expanded nodes', 'Fringe size'])
#
#     # Generate 20 random scenarios
#     for _ in range(20):
#         # Create a random 8-puzzle problem instance
#         puzzle = createRandomEightPuzzle(25)
#         problem = ep.EightPuzzleSearchProblem(puzzle)
#
#         # Get the initial state as a list
#         initial_state = [cell for row in puzzle.cells for cell in row]
#
#         # Write the scenario to the scenarios file
#         scenarios_writer.writerow(initial_state)
#
#         print(f"Scenario: {initial_state}")
#
#         # For each heuristic
#         for heuristic in heuristics:
#             # Solve the problem using A* search with the heuristic
#             actions = search.aStarSearch(problem, heuristic)
#
#             # Record the results (depth, expanded nodes, fringe size)
#             depth = len(actions)
#             expanded_nodes = problem.expandedNodes
#             fringe_size = problem.fringeSize
#
#             # Write the results to the CSV file
#             results_writer.writerow([initial_state, heuristic.__name__, depth, expanded_nodes, fringe_size])



import csv
import eightpuzzle as ep
import search
import random

# Define the heuristics
heuristics = [ep.h1, ep.h2, ep.h3, ep.h4]

def createRandomEightPuzzle(moves=100):
    puzzle = ep.EightPuzzleState([0,1,2,3,4,5,6,7,8])
    for i in range(moves):
        puzzle = puzzle.result(random.choice(puzzle.legalMoves()))
    return puzzle

# Open the results file and scenarios file
with open('results.csv', 'w', newline='') as results_file, open('scenarios.csv', 'w', newline='') as scenarios_file:
    results_writer = csv.writer(results_file)
    scenarios_writer = csv.writer(scenarios_file)

    # Write the header row
    results_writer.writerow(['Scenario', 'Heuristic', 'Depth', 'Expanded nodes', 'Fringe size'])

    # Initialize a dictionary to store the total depth, expanded nodes, and fringe size for each heuristic
    totals = {heuristic.__name__: {'depth': 0, 'expanded_nodes': 0, 'fringe_size': 0} for heuristic in heuristics}

    # Generate 20 random scenarios
    for _ in range(20):
        # Create a random 8-puzzle problem instance
        puzzle = createRandomEightPuzzle(25)
        problem = ep.EightPuzzleSearchProblem(puzzle)

        # Get the initial state as a list
        initial_state = [cell for row in puzzle.cells for cell in row]

        # Write the scenario to the scenarios file
        scenarios_writer.writerow(initial_state)

        print(f"Scenario: {initial_state}")

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
        avg_depth = totals[heuristic.__name__]['depth'] / 20.0
        avg_expanded_nodes = totals[heuristic.__name__]['expanded_nodes'] / 20.0
        avg_fringe_size = totals[heuristic.__name__]['fringe_size'] / 20.0

        print(f"{heuristic.__name__}: Depth {avg_depth}, Expanded nodes {avg_expanded_nodes}, Fringe size {avg_fringe_size}")

    # Decide on the best heuristic based on the averages
    best_heuristic = min(heuristics, key=lambda heuristic: totals[heuristic.__name__]['depth'])
    print(f"\nBest heuristic based on average depth: {best_heuristic.__name__}")