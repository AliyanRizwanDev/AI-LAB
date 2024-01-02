#Task2
from queue import PriorityQueue

def astar(start, goal, h):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not open_set.empty():
        _, current = open_set.get()
        
        if current == goal:
            break
            
        for next_state in neighbors(current):
            new_cost = cost_so_far[current] + 1
            
            if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                cost_so_far[next_state] = new_cost
                priority = new_cost + h(next_state, goal)
                open_set.put((priority, next_state))
                came_from[next_state] = current
                
    if goal not in came_from:
        return None
    
    path = []
    current_state = goal
    while current_state != start:
        path.append(current_state)
        current_state = came_from[current_state]
    path.append(start)
    
    return path[::-1]

def h1(state, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j]:
                count += 1
    return count


def neighbors(state):
    blank_i, blank_j = None, None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                blank_i, blank_j = i, j
                break

    possible_moves = []
    if blank_i > 0:
        possible_moves.append(move_blank(state, blank_i, blank_j, blank_i - 1, blank_j))
    if blank_i < 2:
        possible_moves.append(move_blank(state, blank_i, blank_j, blank_i + 1, blank_j))
    if blank_j > 0:
        possible_moves.append(move_blank(state, blank_i, blank_j, blank_i, blank_j - 1))
    if blank_j < 2:
        possible_moves.append(move_blank(state, blank_i, blank_j, blank_i, blank_j + 1))

    return possible_moves

def move_blank(state, blank_i, blank_j, new_i, new_j):
    new_state = [list(row) for row in state]
    new_state[blank_i][blank_j] = new_state[new_i][new_j]
    new_state[new_i][new_j] = 0
    return tuple(map(tuple, new_state))

# Test the astar function
initial_state = ((2, 1, 3), (4, 7, 6), (5, 8, 0))
goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

path = astar(initial_state, goal_state, h1)
if path is None:
    print("No path found")
else:
    print("Path found using h:")
    for state in path:
        print(state)


