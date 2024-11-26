class Node:
    def __init__(self, name, Heuristic, parent=None, g=0):
        self.name = name        
        self.parent = parent
        self.cost = g
        self.Eval = self.cost + Heuristic[name]
            

def generate_successors(node, romania_map, Heuristic):
    successors = []
    print(f"{node.name} connects to {len(romania_map[node.name])} cities.")
    print('The cities add to successors.')
    for city, distance in romania_map[node.name].items():
        successors.append(Node(city, Heuristic, parent=node, g=node.cost + distance))    
    print('successors of ', node.name, ' : ')
    for i in successors: print(i.name, i.Eval, end=', ')
    print()
    return successors


def extract_solution(node):
    solution = []
    while node:
        solution.append((node.name, node.Eval))
        node = node.parent
    return list(reversed(solution))


def Astar_RomaniaTurism(romania_map, initial_city, Heuristic):
    initial_state = Node(initial_city, Heuristic)  # Start from initial city
    frontier = [initial_state]
    Eval_n = [initial_state.Eval]
    ES = []
    while frontier:
        print('frontier is ', end=' ')
        for i in frontier: print( i.name, ', cost=', i.cost, ', Eval=', i.Eval, end='| ')    
        print('\nE(n) is ', end=' ')
        for i in Eval_n: print( i, end=', ')       
        current_node = frontier.pop(Eval_n.index(min(Eval_n)))  # Selection based on the lowest E(n)
        Eval_n.pop(Eval_n.index(min(Eval_n)))    
        print('\nES = ', ES)
        if (current_node.name) in ES:
            print('visited nodes :', ES)
            print(current_node.name, ' is visited. Go to the next order.')
        else:            
            ES.append(current_node.name)            
            print(current_node.name, ' is added to ES.')
            print('visited nodes :', ES)            
            if current_node.name == 'Bucharest':  # Check the Goal state
                print('The best Evaluation is , ', current_node.Eval)                
                solution = extract_solution(current_node)
                for city, Eval in solution: print(f"{city} (E={Eval})", end=' -> ')
                return solution
            else:
                # move to available citis.
                successors = generate_successors(current_node, romania_map, Heuristic)
                print('len successors : ', len(successors))
                for successor in successors:                
                    if successor.name not in ES: 
                        frontier.append(successor)
                        Eval_n.append([successor.Eval])
        print('Teminate an iteration -----------------------------------------------------')

romania_map = {
    'Arad' : {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Bucharest' : {'Urziceni': 85, 'Pitesti': 101, 'Giurgiu': 90, 'Fagaras': 211},
    'Craiova' : {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Drobeta' : {'Mehadia': 75, 'Craiova': 120},
    'Eforie' : {'Hirsova': 86},
    'Fagaras' : {'Sibiu': 99, 'Bucharest': 211},
    'Giurgiu' : {'Bucharest': 90},
    'Hirsova' : {'Urziceni': 98, 'Eforie': 86},
    'Iasi' : {'Neamt': 87, 'Vaslui': 92},
    'Lugoj' : {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia' : {'Lugoj': 70, 'Drobeta': 75},
    'Neamt' : {'Iasi': 87},
    'Oradea' : {'Zerind': 71, 'Sibiu': 151},
    'Pitesti' : {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Rimnicu Vilcea' : {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Sibiu' : {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara' : {'Arad': 118, 'Lugoj': 111},
    'Urziceni' : {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Vaslui' : {'Iasi': 92, 'Urziceni': 142},
    'Zerind' : {'Arad': 75, 'Oradea': 71}
}

Heuristic = {
    'Arad' : 366, 'Bucharest' : 0, 'Craiova' : 160, 'Drobeta' : 242,
    'Eforie' : 161, 'Fagaras' : 176, 'Giurgiu' : 77, 'Hirsova' : 151,
    'Iasi' : 226, 'Lugoj' : 244, 'Mehadia' : 241, 'Neamt' : 234,
    'Oradea' : 380, 'Pitesti' : 100, 'Rimnicu Vilcea' : 193,
    'Sibiu' : 253, 'Timisoara' : 329, 'Urziceni' : 80, 'Vaslui' : 199,
    'Zerind' : 374
}

Astar_RomaniaTurism(romania_map, 'Arad', Heuristic)

