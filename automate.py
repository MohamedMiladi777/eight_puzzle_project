import csv
import random
import search
from eightpuzzle import EightPuzzleState, EightPuzzleSearchProblem, h1, h2, h3, h4



print("Generating initial states...")

def generate_initial_states(num_states):
    initial_states = []
    print("Generating initial states...")
    for _ in range(num_states):
        puzzle = EightPuzzleState([0, 1, 2, 3, 4, 5, 6, 7, 8])
        num_moves = random.randint(1, 100)  # Generate a random number of moves between 1 and 100
        for _ in range(num_moves):
            legal_moves = puzzle.legalMoves()
            if not legal_moves:
                break  # If there are no legal moves, stop shuffling
            move = random.choice(legal_moves)
            puzzle = puzzle.result(move)  # Apply a random legal move
        initial_states.append(puzzle)
        print(f"Generated initial state {len(initial_states)}")

    return initial_states




def solve_puzzle_with_heuristic(initial_states, heuristic_fn):
    results = []
    for initial_state in initial_states:
        problem = EightPuzzleSearchProblem(initial_state)
        path = search.aStarSearch(problem, heuristic_fn)
        depth = len(path)
        expanded_nodes = problem.expandedNodes
        fringe_size = problem.fringeSize
        results.append((depth, expanded_nodes, fringe_size))
    return results

# def save_results_to_csv(results, heuristic_name):
#     filename = f"results_{heuristic_name}.csv"
#     with open(filename, mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(["Depth", "Expanded Nodes", "Fringe Size"])
#         for depth, expanded_nodes, fringe_size in results:
#             writer.writerow([depth, expanded_nodes, fringe_size])
import os

print("Generating initial states...")

def save_results_to_csv(results, heuristic_name):
    # Specify the absolute file path where you want to save the CSV files
    file_path = os.path.join(os.getcwd(), f"results_{heuristic_name}.csv")

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Depth", "Expanded Nodes", "Fringe Size"])
        for depth, expanded_nodes, fringe_size in results:
            writer.writerow([depth, expanded_nodes, fringe_size])


if __name__ == '__main__':
    num_states = 100  # You can change this to the number of initial states you want to generate
    initial_states = generate_initial_states(num_states)

    # Solve using h1 heuristic
    h1_results = solve_puzzle_with_heuristic(initial_states, h1)
    save_results_to_csv(h1_results, "h1")

    # Solve using h2 heuristic
    h2_results = solve_puzzle_with_heuristic(initial_states, h2)
    save_results_to_csv(h2_results, "h2")

    # Solve using h3 heuristic
    h3_results = solve_puzzle_with_heuristic(initial_states, h3)
    save_results_to_csv(h3_results, "h3")

    # Solve using h4 heuristic
    h4_results = solve_puzzle_with_heuristic(initial_states, h4)
    save_results_to_csv(h4_results, "h4")

    print("Results saved to CSV files.")
