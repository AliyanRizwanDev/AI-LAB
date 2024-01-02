#BFS
def BFS(graph,start,goal):
    queue = []
    expanded = []
    if start not in expanded:
        queue.append(start)
    while queue != []:
        deque = queue.pop(0)
        expanded.append(deque)
        if deque == goal:
            print(expanded)
            break;
        
        for neighbour in sorted(graph[deque]):
            
            if neighbour not in expanded:
                queue.append(neighbour)
        
            
graph = {
    'A' : {'B','C'},
    'B' : {'D','E'},
    'D' : {}, 'E' : {},
    'C' : {'F','G'},
    'F' : {},'G':{}
}
start = 'A'
goal = 'G'

BFS(graph,start,goal)
        