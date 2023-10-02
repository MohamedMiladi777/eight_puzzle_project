import csv
from NxNpuzzle import NPuzzleState, NPuzzleSearchProblem, h1, h2, h3, h4, createRandomNPuzzle
import search

# Define the search strategies
strategies = [search.dfs, search.bfs, search.aStarSearch]
best_heuristic = h1  # Replace with your best heuristic for NxN puzzles

# Define the puzzle sizes
puzzle_sizes = [3, 4, 5]  # You can add more sizes as needed

# Open the results file
with open('BestSearchResultsNxN.csv', 'w', newline='') as results_file:
    results_writer = csv.writer(results_file)

    # Write the header row
    results_writer.writerow(['Scenario', 'Strategy', 'Depth', 'Expanded nodes', 'Fringe size'])

    # Initialize a dictionary to store the total depth, expanded nodes, and fringe size for each strategy
    totals = {strategy.__name__: {'depth': 0, 'expanded_nodes': 0, 'fringe_size': 0} for strategy in strategies}

    # Generate random scenarios for each puzzle size
    for size in puzzle_sizes:
        for _ in range(20):  # Generate 20 random scenarios for each size
            # Create a random solvable NxN puzzle problem instance
            puzzle = createRandomNPuzzle(size, 50)  # Adjust the number of random moves as needed
            problem = NPuzzleSearchProblem(puzzle)

            # Get the initial state as a list
            initial_state = [cell for row in puzzle.cells for cell in row]

            print(f"\nScenario (Size {size}x{size}): {initial_state}")

            # For each strategy
            for strategy in strategies:
                print(f"Applying {strategy.__name__}...")
                if strategy == search.aStarSearch:
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

                # Add the results to the totals for this strategy
                totals[strategy.__name__]['depth'] += depth
                totals[strategy.__name__]['expanded_nodes'] += expanded_nodes
                totals[strategy.__name__]['fringe_size'] += fringe_size

                # Write the results to the CSV file
                results_writer.writerow([initial_state, strategy.__name__, depth, expanded_nodes, fringe_size])

    # Calculate and print the average results for each strategy
    print("\nAverage results for each strategy:")
    for strategy in strategies:
        avg_depth = totals[strategy.__name__]['depth'] / (20 * len(puzzle_sizes))
        avg_expanded_nodes = totals[strategy.__name__]['expanded_nodes'] / (20 * len(puzzle_sizes))
        avg_fringe_size = totals[strategy.__name__]['fringe_size'] / (20 * len(puzzle_sizes))

        print(f"{strategy.__name__}: Depth {avg_depth}, Expanded nodes {avg_expanded_nodes}, Fringe size {avg_fringe_size}")
