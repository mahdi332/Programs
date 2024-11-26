class Node:
    def __init__(self, position, state, parent=None, action=None, d=0, number=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.position_agent = position
        self.num_node = number
        self.depth = d


def generate_successors(node):
    successors = []
    if node.position_agent == 0:
        print('For node ', node.num_node, ' = ', node.state, ' and agent in ', node.position_agent)
        print('There are at most 2 actions Right and Suck.')
        print('Run the actions and add new states to the edd of successors.')
        successors.append(Node(node.position_agent + 1, node.state, parent=node, action="Right", d=node.depth + 1))
        if node.state[node.position_agent] == 'D':
            s = node.state.copy()
            s[node.position_agent] = 'C'            
            successors.append(Node(node.position_agent, s, parent=node, action="Suck", d=node.depth + 1))
    elif node.position_agent == len(node.state) - 1:
        print('for node ', node.num_node, ' = ', node.state, ', there are at most 2 actions Left and Suck.')
        print('Run the actions and add new states to the edd of successors.')
        successors.append(Node(node.position_agent - 1, node.state, parent=node, action="Left", d=node.depth + 1))
        if node.state[node.position_agent] == 'D':
            s = node.state.copy()
            s[node.position_agent] = 'C'            
            successors.append(Node(node.position_agent, s, parent=node, action="Suck", d=node.depth + 1))
    else:
        print('for node ', node.num_node, ' = ', node.state, ', there are at most 3 actions Left, Right and Suck.')
        print('Run the actions and add new states to the edd of successors.')
        successors.append(Node(node.position_agent - 1, node.state, parent=node, action="Left", d=node.depth + 1))
        successors.append(Node(node.position_agent + 1, node.state, parent=node, action="Right", d=node.depth + 1))
        if node.state[node.position_agent] == 'D':
            s = node.state.copy()
            s[node.position_agent] = 'C'            
            successors.append(Node(node.position_agent, s, parent=node, action="Suck", d=node.depth + 1))
    return successors


def extract_solution(node, solution):
    while node.num_node:        
        solution.append(node.state)
        solution.append(node.position_agent)
        solution.append(node.action)        
        node = node.parent        
    solution.append(node.state)
    solution.reverse()
    return solution


def dls_vacuum_cleaner(environment, initial_position, limited_depth):
    initial_state = Node(initial_position, environment)  # Start from initial position
    frontier, num = [initial_state], 0
    ES = []
    solution = []
    while frontier:
        print('frontier is ', end=' ')
        for i in frontier: print( i.position_agent, i.state, end=', ')
        print()
        current_node = frontier.pop()    # Selection based on LIFO    
        print('ES = ', ES)
        if ([current_node.position_agent, current_node.state]) in ES:
            print('visited nodes :', ES)
            print(current_node.position_agent, ' agent in', current_node.state, ' is visited. Go to the next order.')
        elif current_node.depth >= limited_depth:    # Check the limited depth
            print(current_node.position_agent, ' agent in', current_node.state, ' has reached a limited depth and becomes a leaf.')            
        else:            
            ES.append([current_node.position_agent, current_node.state])
            print(current_node.position_agent, ' agent in', current_node.state, ' is added to ES.')
            print('visited nodes :', ES)
            # The order of action is Left, Right, Suck
            successors = generate_successors(current_node)
            print('len successors : ', len(successors))
            for i in successors:
                print(i.state, ',   ', i.position_agent, ',   ', i.action)
            for successor in successors:
                # Check the Goal state
                if successor.state == ['C', 'C']:
                    print('Agent achieves to Goal')
                    num += 1
                    successor.num_node = num
                    solution = extract_solution(successor, solution)
                    print('Solution is :', solution)
                    return solution
                elif successor not in ES: 
                    num += 1
                    successor.num_node = num
                    frontier.append(successor)
        print('Teminate an iteration -----------------------------------------------------')
    else:
        print('The problem in the limited depth', limited_depth, ' could not reach to the goal!')
        
environment = ['D', 'D']
dls_vacuum_cleaner(environment, 0, 2)
