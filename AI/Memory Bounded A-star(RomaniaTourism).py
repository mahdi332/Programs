class Node:
    def __init__(self, name, Heuristic, parent=None, g=0):
        self.name = name
        self.parent = parent
        self.cost = g  # g(n): cost from start to current node
        self.Eval = self.cost + Heuristic[name]  # E(n) = g(n) + h(n)
        self.forgotten_eval = None  # This stores the best E(n) of pruned nodes

def generate_successors(node, romania_map, Heuristic):
    successors = []
    print(f"{node.name} connects to {len(romania_map[node.name])} cities.")
    print('The cities add to successors.')
    for city, distance in romania_map[node.name].items():
        successors.append(Node(city, Heuristic, parent=node, g=node.cost + distance))    
    print('successors of ', node.name, ' : ', end=' ')
    for i in successors: print(i.name, i.Eval, end=', ')
    print()
    return successors

def extract_solution(node):
    solution = []
    while node:
        solution.append((node.name, node.Eval))
        node = node.parent
    return list(reversed(solution))

def get_best_forgotten(successors):  # Helper function to update best forgotten node's eval
    return min([s.forgotten_eval for s in successors if s.forgotten_eval is not None], default=float('inf'))

# Function to backtrack if pruned nodes offer a better solution
def backtrack_or_continue(current_node, memory_limit, frontier, Eval_n, ES, pruned_Eval_n):
    # If the current node has a forgotten eval and it's better than current eval
    if current_node.forgotten_eval and (current_node.forgotten_eval < current_node.Eval):
        # If the pruned node's eval is better, backtrack by inserting back in the frontier
        print(f"Backtracking: Node {current_node.name} has a forgotten Eval of {current_node.forgotten_eval}")
        current_node.Eval = current_node.forgotten_eval  # Update Eval with pruned node value
        frontier.append(current_node)
        Eval_n.append(current_node.Eval)
        return True  # Backtracked, need to reconsider the node
    return False  # No backtracking needed, continue with current node

def MAstar_RomaniaTurism(romania_map, initial_city, Heuristic, memory_limit):
    initial_state = Node(initial_city, Heuristic)
    frontier, Eval_n, ES  = [initial_state], [initial_state.Eval], []
    pruned_Eval_n = {}  # Store pruned nodes and their E(n) for possible backtracking
    while frontier:
        print('Current Frontier:', end=' | ')
        for node in frontier: print(f"{node.name}, Cost: {node.cost}, Eval: {node.Eval}", end=' | ')
        print('\nE(n) is ', end=' | ')
        for i in Eval_n: print(i, end=' | ')
        print('\nES = ', ES)
        current_node = frontier.pop(Eval_n.index(min(Eval_n))) # Pop node with lowest Eval
        Eval_n.pop(Eval_n.index(min(Eval_n)))        
        if current_node.name == 'Bucharest':  # Goal check
            print("Goal reached!")
            solution = extract_solution(current_node)
            for city, Eval in solution:
                print(f"{city} (Eval={Eval})", end=' -> ')
            return solution
        
        # Backtracking: If a pruned node has a better evaluation, reconsider it
        if backtrack_or_continue(current_node, memory_limit, frontier, Eval_n, ES, pruned_Eval_n):
            continue  # Skip the rest of the loop and reprocess the backtracked node
        
        if current_node.name in ES:
            print('visited nodes :', ES)
            print(current_node.name, ' is visited. Go to the next order.')
            continue 
        ES.append(current_node.name)  # Add the current node to ES           
        print(current_node.name, ' is added to ES.')
        print('visited nodes :', ES)        
        successors = generate_successors(current_node, romania_map, Heuristic)
        print('len successors : ', len(successors))
        for successor in successors:  # Add new successors to frontier
            if successor.name not in ES:            
                if len(frontier) >= memory_limit: # Check memory limit and prune if necessary
                    print("Memory limit reached. Pruning a node from the frontier.")                    
                    max_eval_index = Eval_n.index(max(Eval_n)) # Find the node with the highest Eval to prune
                    pruned_node = frontier.pop(max_eval_index)  # Prune the worst node from frontier
                    Eval_n.pop(max_eval_index)                  # Update Eval_n based on pruned node  
                    print(f"Memory limit exceeded! Pruning {pruned_node.name} (Eval={pruned_node.Eval})")
                    pruned_Eval_n[pruned_node.name] = pruned_node.Eval
                    best_forgotten_eval = get_best_forgotten(successors)
                    pruned_node.parent.forgotten_eval = min(pruned_node.Eval, best_forgotten_eval)
                    print(f"The parent of pruned node is {pruned_node.parent.name} wiht forgotten Eval={pruned_node.parent.forgotten_eval})")
                frontier.append(successor)
                Eval_n.append(successor.Eval)
                print('Updated Frontier:', end=' | ')
                for node in frontier: print(f"{node.name}, Cost: {node.cost}, Eval: {node.Eval}", end=' | ')
                print('\nUpdated E(n) is ', end=' | ')
                for i in Eval_n: print(i, end=' | ')
                print()                 
        print("---- End of iteration ----")
    else:
        print("No solution found")
        return None

romania_map = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Bucharest': {'Urziceni': 85, 'Pitesti': 101, 'Giurgiu': 90, 'Fagaras': 211},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Eforie': {'Hirsova': 86},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Giurgiu': {'Bucharest': 90},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Iasi': {'Neamt': 87, 'Vaslui': 92},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Neamt': {'Iasi': 87},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Zerind': {'Arad': 75, 'Oradea': 71}
}

Heuristic = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242,
    'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151,
    'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
    'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
    'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199,
    'Zerind': 374
}

memory_limit = 4  
MAstar_RomaniaTurism(romania_map, 'Arad', Heuristic, memory_limit)
