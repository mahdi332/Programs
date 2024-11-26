class Node:
    def __init__(self, name, Heuristic, parent=None, g=0):
        self.name = name        
        self.parent = parent
        self.cost = g
        self.Eval = self.cost + Heuristic[name]


def generate_successors(node, romania_map, Heuristic):
    successors = []
    print(node.name, ' conects to ', len(romania_map[node.name]), ' cities.')
    print('The cities add to successors.')
    for i in romania_map[node.name]:        
        successors.append(Node(i, Heuristic, parent=node, g=node.cost + romania_map[node.name][i]))    
    print('successors of ', node.name, ' : ')
    for i in successors: 
        print(i.name, i.Eval, end=', ')
    print()
    return successors


def IDAstar_RomaniaTurism(romania_map, initial_city, Heuristic):
    def depth_first_search(ES, Cut_off, romania_map, Heuristic):        
        node = ES[-1]  # Select based on LIFO
        print('\n\nRunning depth first search for ', node.name, '----------------')
        print('ES is |', end=' ')
        for i in ES: print( i.name, ', cost=', i.cost, ', Eval=', i.Eval, end='| ')
        print('\ncut_off is ', Cut_off)
        if node.Eval > Cut_off:
            print(f"E({node.name}) = {node.Eval} is bigger than cut_off ={Cut_off}")
            print('So, depth first search is terminated and return a integer value!')
            return node.Eval
        if node.name == 'Bucharest':
            print('depth first search reach to goal and return solution')
            return ES
        min_Eval = float('inf')
        successors = generate_successors(node, romania_map, Heuristic)
        print('len successors : ', len(successors))
        for successor in successors:
             if successor.name not in [n.name for n in ES]:        
                ES.append(successor)
                temp = depth_first_search(ES, Cut_off, romania_map, Heuristic)
                if isinstance(temp, list):
                    print('Depth first search terminates and returns a part of potential solution.')
                    return temp
                if temp < min_Eval:
                    print('Depth first search terminates and returns the value that exceeded cut_off.')
                    min_Eval = temp
                print(ES[-1].name, ' which was added to the end of ES, remove from it!')
                ES.pop()
        return min_Eval

    initial_state = Node(initial_city, Heuristic)  # Start from initial city
    Cut_off = initial_state.Eval
    ES = [initial_state]
    while True:
        temp = depth_first_search(ES, Cut_off, romania_map, Heuristic)
        if isinstance(temp, list):
            return temp
        if temp == float('inf'):
            return None
        Cut_off = temp

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
    'Arad': 366, 'Zerind': 374, 'Oradea': 380, 'Sibiu': 253,
    'Timisoara': 329, 'Lugoj': 244, 'Mehadia': 241, 'Drobeta': 242,
    'Craiova': 160, 'Rimnicu Vilcea': 193, 'Fagaras': 178, 'Pitesti': 98,
    'Bucharest': 0, 'Giurgiu': 77
}


solution = IDAstar_RomaniaTurism(romania_map, 'Arad', Heuristic)

if solution:
    print("solution found:")
    for node in solution:
        print(node.name, end=" -> ")
else:
    print("No solution found")
