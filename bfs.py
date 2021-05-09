import queue


def bfs(adj, start):
    visited = set()
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        u = q.get()
        print(u)
        for v in adj.get(u, []):
            if v not in visited:
                visited.add(v)
                q.put(v)

def dfs(graph, start):
    visited = []
    stack = []
    stack.append(start)
    print(stack)
    while stack != []:
        node = stack.pop()
        print(node)
        for v in graph.get(node, []):
            if v not in visited:
                visited.append(v)
                stack.append(v)

graph = {1: [2, 4], 2: [4, 3], 3: [4], 4: [5]}
#bfs(graph, 1)
dfs(graph, 1)
