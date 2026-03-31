# Step 1: Define variables (states)
states = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

# Step 2: Define domain (colors)
colors = ['Red', 'Green', 'Blue']

# Step 3: Define constraints (neighbors)
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

# Function to check if assignment is valid
def is_valid(state, color, assignment):
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking function
def backtrack(assignment):
    if len(assignment) == len(states):
        return assignment

    # Select unassigned state
    for state in states:
        if state not in assignment:
            break

    # Try each color
    for color in colors:
        if is_valid(state, color, assignment):
            assignment[state] = color

            result = backtrack(assignment)
            if result:
                return result

            # Backtrack
            del assignment[state]

    return None

# Solve CSP
solution = backtrack({})

# Print result
if solution:
    print("Solution:")
    for state in solution:
        print(state, "=", solution[state])
else:
    print("No solution found")
