class MazeAgent:
    def __init__(self, start, goal, maze):
        self.position = start
        self.goal = goal
        self.maze = maze
        self.path = []

    def perceive(self):
        return self.position

    def act(self):
        if self.position == self.goal:
            return 'GoalReached'
        # Simple right-hand rule for maze solving
        x, y = self.position
        if self.maze[x][y+1] == 0:  # Move right
            return 'Right'
        elif self.maze[x+1][y] == 0:  # Move down
            return 'Down'
        elif self.maze[x][y-1] == 0:  # Move left
            return 'Left'
        elif self.maze[x-1][y] == 0:  # Move up
            return 'Up'

    def update_position(self, action):
        x, y = self.position
        if action == 'Right':
            self.position = (x, y+1)
        elif action == 'Down':
            self.position = (x+1, y)
        elif action == 'Left':
            self.position = (x, y-1)
        elif action == 'Up':
            self.position = (x-1, y)
        self.path.append(self.position)

# Maze setup (0 = path, 1 = wall)
maze = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1]
]

agent = MazeAgent(start=(1, 1), goal=(3, 3), maze=maze)

while agent.position != agent.goal:
    percept = agent.perceive()
    action = agent.act()
    print(f"Position: {percept}, Action: {action}")
    agent.update_position(action)

print("Path to goal:", agent.path)
