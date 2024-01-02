#DFS
def DFS(graph,start,goal):
    stack = []
    expanded = []
    if start not in expanded:
        stack.append(start)
    while stack != []:
        popped = stack.pop()
        expanded.append(popped)
        if popped == goal:
            print(expanded)
            break;
        for neighbour in sorted(graph[popped], reverse=True):
            if neighbour not in expanded:
                stack.append(neighbour)
        
            
graph = {
    'A' : {'B','C'},
    'B' : {'D','E'},
    'D' : {}, 'E' : {},
    'C' : {'F','G'},
    'F' : {},'G':{}
}
start = 'A'
goal = 'G'

DFS(graph,start,goal)
        