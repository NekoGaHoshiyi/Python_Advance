class BTree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def PreOder(self):
        print(self.val, end=' ')
        self.PreOder(self.left)
        self.PreOder(self.right)
    def InOder(self):
        self.PreOder(self.left)
        print(self.val, end=' ')
        self.PreOder(self.right)
    def BacOder(self):
        self.PreOder(self.left)
        self.PreOder(self.right)
        print(self.val, end=' ')
    # 层次遍历，BFS,广度优先
    def BFS(self, root):
        if root == None:
            return
        queue = []
        queue.append(root)
        while queue:
            # 拿出队首
            currentNode = queue.pop(0)
            print(currentNode.val, end=' ')
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
    def DFS(self, root):
        if root == None:
            return
        stack = []
        stack.append(root)
        while stack:
            # 拿出栈顶节点
            currentNode = stack.pop()
            print(currentNode.val, end=' ')
            if currentNode.right:
                stack.append(currentNode.right)
            if currentNode.left:
                stack.append(currentNode.left)