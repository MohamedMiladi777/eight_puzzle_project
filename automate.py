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
import csv
import eightpuzzle as ep
import search

# Define the heuristics
heuristics = [ep.h1, ep.h2, ep.h3, ep.h4]

# Open the scenarios file
with open('scenarios.csv', 'r') as scenarios_file:
    scenarios = csv.reader(scenarios_file)

    # Open the results file
    with open('results.csv', 'w', newline='') as results_file:
        results_writer = csv.writer(results_file)

        # Write the header row
        results_writer.writerow(['Scenario', 'Heuristic', 'Depth', 'Expanded nodes', 'Fringe size'])

        # For each scenario
        for scenario in scenarios:
            if scenario:  # Skip empty lines
                # Parse the scenario to get the initial state
                initial_state = list(map(int, scenario))
                print(f"Scenario: {initial_state}")  # Add this line

                # Create an 8-puzzle problem instance
                puzzle = ep.EightPuzzleState(initial_state)
                problem = ep.EightPuzzleSearchProblem(puzzle)

                # For each heuristic
                for heuristic in heuristics:
                    # Solve the problem using A* search with the heuristic
                    actions = search.aStarSearch(problem, heuristic)

                    # Record the results (depth, expanded nodes, fringe size)
                    depth = len(actions)
                    expanded_nodes = problem.expandedNodes
                    fringe_size = problem.fringeSize

                    # Write the results to the CSV file
                    results_writer.writerow([initial_state, heuristic.__name__, depth, expanded_nodes, fringe_size])
