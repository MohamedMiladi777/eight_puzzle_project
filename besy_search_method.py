import csv
import eightpuzzle as ep
import search

# Define the search strategies
strategies = [search.dfs, search.bfs, search.aStarSearch]
    ##,search.uniformCostSearch, search.astar ]

# Define the best heuristic from Task 2
best_heuristic = ep.h1  # Replace with your best heuristic

# Open the scenarios file and read all scenarios
with open('scenarios.csv', 'r') as scenarios_file:
    scenarios = list(csv.reader(scenarios_file))

# Open the results file
with open('BestSearchResults.csv', 'w', newline='') as results_file:
    results_writer = csv.writer(results_file)

    # Write the header row
    results_writer.writerow(['Scenario', 'Strategy', 'Depth', 'Expanded nodes', 'Fringe size'])

    # For each scenario
    for scenario in scenarios:
        if scenario:  # Skip empty lines
            # Parse the scenario to get the initial state
            initial_state = list(map(int, scenario))
            print(f"\nScenario: {initial_state}")

            # Create an 8-puzzle problem instance
            puzzle = ep.EightPuzzleState(initial_state)
            problem = ep.EightPuzzleSearchProblem(puzzle)

            # For each strategy
            for strategy in strategies:
                print(f"Applying {strategy.__name__}...")
                if strategy == search.astar:
                    # Use the best heuristic for A* search
                    actions = strategy(problem, heuristic=best_heuristic)
                else:
                    # Use the strategy without a heuristic
                    actions = strategy(problem)

                # Record the results (depth, expanded nodes, fringe size)
                depth = len(actions)
                expanded_nodes = problem.expandedNodes
                fringe_size = problem.fringeSize

                print(f"Depth: {depth}, Expanded nodes: {expanded_nodes}, Fringe size: {fringe_size}")

                # Write the results to the CSV file
                results_writer.writerow([initial_state, strategy.__name__, depth, expanded_nodes, fringe_size])
