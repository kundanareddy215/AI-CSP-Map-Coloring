# Telangana Map Coloring using CSP (Backtracking + Visualization)

# Step 1: Variables (districts)
districts = [
    'Adilabad', 'Nizamabad', 'Karimnagar', 'Warangal',
    'Khammam', 'Nalgonda', 'Mahbubnagar', 'Hyderabad'
]

# Step 2: Domain (colors)
colors = ['Red', 'Green', 'Blue']

# Step 3: Constraints (neighbors)
neighbors = {
    'Adilabad': ['Nizamabad', 'Karimnagar'],
    'Nizamabad': ['Adilabad', 'Karimnagar', 'Hyderabad'],
    'Karimnagar': ['Adilabad', 'Nizamabad', 'Warangal'],
    'Warangal': ['Karimnagar', 'Khammam', 'Nalgonda'],
    'Khammam': ['Warangal', 'Nalgonda'],
    'Nalgonda': ['Warangal', 'Khammam', 'Hyderabad', 'Mahbubnagar'],
    'Mahbubnagar': ['Nalgonda', 'Hyderabad'],
    'Hyderabad': ['Nizamabad', 'Nalgonda', 'Mahbubnagar']
}

# Step 4: Check if assignment is valid
def is_valid(district, color, assignment):
    for neighbor in neighbors[district]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Step 5: Backtracking algorithm
def backtrack(assignment):
    if len(assignment) == len(districts):
        return assignment

    # Select unassigned district
    for district in districts:
        if district not in assignment:
            break

    # Try colors
    for color in colors:
        if is_valid(district, color, assignment):
            assignment[district] = color

            result = backtrack(assignment)
            if result:
                return result

            # Backtrack
            del assignment[district]

    return None

# Step 6: Solve CSP
solution = backtrack({})

# Step 7: Print solution (FIXED FORMAT)
print("Solution:")
for district in districts:
    print(f"{district} = {solution[district]}")


# ---------------- VISUALIZATION ----------------

import networkx as nx
import matplotlib.pyplot as plt

# Create graph
G = nx.Graph()

# Add edges
for d in neighbors:
    for n in neighbors[d]:
        G.add_edge(d, n)

# Assign colors
color_map = [solution[node].lower() for node in G.nodes()]

# Draw graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color=color_map,
        node_size=2000, font_size=8)

plt.title("Telangana Map Coloring (CSP Visualization)")
plt.show()
