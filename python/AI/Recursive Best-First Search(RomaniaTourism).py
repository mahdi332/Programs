class Node:
    def __init__(self, name, heuristic, parent=None, g=0):
        self.name = name
        self.parent = parent
        self.cost = g
        self.Eval = self.cost + heuristic[name]


def generate_successors(node, romania_map, heuristic):
    successors = []
    print(f"{node.name} connects to {len(romania_map[node.name])} cities.")
    print("The cities are added to successors.")
    for city, distance in romania_map[node.name].items():
        successors.append(Node(city, heuristic, parent=node, g=node.cost + distance))
    print(f"Successors of {node.name}: ")
    for i in successors:
        print(f"{i.name} (f={i.Eval})", end=", ")
    print()
    return successors


def extract_solution(node):
    solution = []
    while node:
        solution.append((node.name, node.Eval))
        node = node.parent
    return list(reversed(solution))


def rbfs(node, Tag, romania_map, heuristic):
    print(f"\nExploring {node.name} with E={node.Eval}, Tag={Tag}---------")
    if node.name == "Bucharest":
        return node, node.Eval
    successors = generate_successors(node, romania_map, heuristic)
    if not successors:
        return None, float("inf")
    for s in successors:
        s.Eval = max(s.Eval, node.Eval)
        print("en ba pedar avaz shod")
    while True:
        successors.sort(key=lambda x: x.Eval)
        best = successors[0]
        if best.Eval > Tag:
            print(f"Best successor {best.name} exceeds Tag {Tag}")
            print("Search is transferred to the peer node with the tag matching E(n).")
            return None, best.Eval
        alternative = successors[1].Eval if len(successors) > 1 else Tag
        print(f"Recursing on {best.name} with Tag={min(Tag, alternative)}")
        result, best.Eval = rbfs(best, min(Tag, alternative), romania_map, heuristic)
        if result is not None:
            print(f"result = {result.name} with E({result.Eval})")
            return result, best.Eval


def rbfs_romania_tourism(romania_map, initial_city, heuristic):
    initial_node = Node(initial_city, heuristic)
    result, _ = rbfs(initial_node, float("inf"), romania_map, heuristic)
    if result:
        solution = extract_solution(result)
        print("Solution found:")
        for city, Eval in solution:
            print(f"{city} (E={Eval})", end=" -> ")
        return solution
    else:
        print("No solution found")
        return None


romania_map = {
    "Arad": {"Zerind": 75, "Sibiu": 140, "Timisoara": 118},
    "Bucharest": {"Urziceni": 85, "Pitesti": 101, "Giurgiu": 90, "Fagaras": 211},
    "Craiova": {"Drobeta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
    "Drobeta": {"Mehadia": 75, "Craiova": 120},
    "Eforie": {"Hirsova": 86},
    "Fagaras": {"Sibiu": 99, "Bucharest": 211},
    "Giurgiu": {"Bucharest": 90},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Iasi": {"Neamt": 87, "Vaslui": 92},
    "Lugoj": {"Timisoara": 111, "Mehadia": 70},
    "Mehadia": {"Lugoj": 70, "Drobeta": 75},
    "Neamt": {"Iasi": 87},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Pitesti": {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucharest": 101},
    "Rimnicu Vilcea": {"Sibiu": 80, "Craiova": 146, "Pitesti": 97},
    "Sibiu": {"Arad": 140, "Oradea": 151, "Fagaras": 99, "Rimnicu Vilcea": 80},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Urziceni": {"Bucharest": 85, "Vaslui": 142, "Hirsova": 98},
    "Vaslui": {"Iasi": 92, "Urziceni": 142},
    "Zerind": {"Arad": 75, "Oradea": 71},
}

heuristic = {
    "Arad": 366,
    "Bucharest": 0,
    "Craiova": 160,
    "Drobeta": 242,
    "Eforie": 161,
    "Fagaras": 176,
    "Giurgiu": 77,
    "Hirsova": 151,
    "Iasi": 226,
    "Lugoj": 244,
    "Mehadia": 241,
    "Neamt": 234,
    "Oradea": 380,
    "Pitesti": 100,
    "Rimnicu Vilcea": 193,
    "Sibiu": 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vaslui": 199,
    "Zerind": 374,
}

rbfs_romania_tourism(romania_map, "Arad", heuristic)
