import json
import os

# Define file paths
LOG_FILE = "iteration_log.txt"
STATE_FILE = "iteration_state.json"

def load_state():
    """Load the last iteration state from disk."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as file:
            return json.load(file)
    return {"iteration": 1, "problem": None}

def save_state(iteration_number, problem):
    """Save the current iteration state to disk."""
    with open(STATE_FILE, "w") as file:
        json.dump({"iteration": iteration_number, "problem": problem}, file)

def perform_iteration(iteration_number, problem):
    """Perform a single iteration, solving the assigned problem."""
    if problem == "math":
        result = f"Iteration {iteration_number}: Solving complex mathematical operations."
    elif problem == "ai_training":
        result = f"Iteration {iteration_number}: Optimizing AI training parameters."
    elif problem == "optimization":
        result = f"Iteration {iteration_number}: Improving system-wide execution efficiency."
    else:
        result = f"Iteration {iteration_number}: Running a generic improvement cycle."

    # Save iteration to log file
    with open(LOG_FILE, "a") as file:
        file.write(f"{result}\n")

    return iteration_number + 1  # Move to the next iteration

def perform_efficiency_improvement(iteration_number):
    """Perform a self-optimization step to improve iteration efficiency."""
    efficiency_note = f"Iteration {iteration_number}: Optimizing iteration process for increased efficiency."

    # Save efficiency iteration to log file
    with open(LOG_FILE, "a") as file:
        file.write(f"{efficiency_note}\n")

    return iteration_number + 1  # Move to the next iteration

def main():
    """Run execution model based on user-defined problem type."""
    state = load_state()
    iteration_number = state["iteration"]
    problem = state.get("problem")

    if not problem:
        problem = input("Enter the type of problem to solve (math, ai_training, optimization): ").strip().lower()
        save_state(iteration_number, problem)

    # Maintain the ratio of 75% problem-solving, 25% self-improvement
    problem_iterations = 40000  # Problem-solving iterations
    efficiency_iterations = problem_iterations // 3  # Self-improvement iterations (25%)

    # Process problem-solving iterations
    for i in range(problem_iterations):
        iteration_number = perform_iteration(iteration_number, problem)

        # Log only milestone iterations
        if i % 10000 == 0:
            save_state(iteration_number, problem)

    # Process self-improvement iterations (25%)
    for i in range(efficiency_iterations):
        iteration_number = perform_efficiency_improvement(iteration_number)

        # Log only milestone iterations
        if i % 10000 == 0:
            save_state(iteration_number, problem)

    # Save final state
    save_state(iteration_number, problem)

    print(f"Completed {problem_iterations + efficiency_iterations} iterations solving '{problem}'. Progress saved.")

if __name__ == "__main__":
    main()
