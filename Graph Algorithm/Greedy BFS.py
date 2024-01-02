#TASK1
from queue import PriorityQueue

def greedy_bfs(start, goal, h):
    frontier = PriorityQueue()
    frontier.put((start, 0))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current, _ = frontier.get()

        if current == goal:
            break

        for next_state in neighbors(current):
            new_cost = cost_so_far[current] + 1

            if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                cost_so_far[next_state] = new_cost
                priority = h(next_state, goal)
                frontier.put((next_state, priority))
                came_from[next_state] = current

    return came_from, cost_so_far

def h1(state, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j]:
                count += 1
    return count

def h2(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0:
                goal_i, goal_j = divmod(tile - 1, 3)
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance


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

initial_state = ((2, 1, 3), (4, 7, 6), (5, 8, 0))
goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

came_from, cost_so_far = greedy_bfs(initial_state, goal_state, h1)
if goal_state not in came_from:
    print("Goal state not found.")
else:
    print("Goal state found!")
    print("Steps to reach the goal state:")
    current_state = goal_state
    path = [current_state]
    while current_state != initial_state:
        current_state = came_from[current_state]
        path.append(current_state)
    path.reverse()
    for state in path:
        print(state)