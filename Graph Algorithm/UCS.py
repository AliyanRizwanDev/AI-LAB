#Task3
from queue import PriorityQueue

def ucs(graph, start, goal):
    queue = PriorityQueue()
    queue.put((0, start))
    expanded = []
    cost_so_far = {start: 0}

    while not queue.empty():
        current_cost, current_node = queue.get()
        expanded.append(current_node)

        if current_node == goal:
            print("Expanded nodes:", expanded)
            print("Path cost:", cost_so_far[current_node])
            break

        for neighbor, cost in graph[current_node].items():
            new_cost = cost_so_far[current_node] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                queue.put((new_cost, neighbor))

    return None


graph = {
    'S': {'A': 3, 'C': 2, 'D': 2},
    'A': {},
    'B': {'E': 2},
    'C': {'F': 1},
    'D': {'B': 3, 'G': 8},
    'E': {'G': 2},
    'F': {'E': 0, 'G': 4},
    'G': {}
}

start = 'S'
goal = 'G'

ucs(graph, start, goal)
