class NodeMap:
    def __init__(self):
        self.graph = {}
    def findOrder(self, nodeCount, edges):
        for i in range(nodeCount):
            self.graph[i] = []
            for e in edges:
                if e[0] == i:
                    self.graph[i].append(e[1])
        print(self.graph)
        # 寻找起点root
        sourceset = set()
        targetset = set()
        for e in edges:
            sourceset.add(e[0])
            targetset.add(e[1])
        root = (sourceset - targetset).pop()
        visited = []
        stack = []
        stack.append(root)
        trace = []
        while stack != []:
            print(stack)
            c = stack.pop()
            trace.append(c)
            for v in self.graph.get(c, []):
                if v not in visited:
                    visited.append(v)
                    stack.append(v)
        return trace
node = NodeMap()
print(node.findOrder(nodeCount=4, edges=[[0,1],[0,2],[3,0],[2,1]]))
