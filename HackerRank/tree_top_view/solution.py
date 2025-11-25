class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    #Write your code here
    # Breadth First Search Method
    from collections import deque
    
    # Create an empty queue Q 
    Q = deque([])
    result = {}
    
    # Enqueue the root node of the tree to Q
    Q.append((root, 0))
    
    # Loop while Q is not empty
    while Q:
    #   Dequeue a node from Q and visit it
        node, hd = Q.popleft()
        if node == None:
            continue
        
        if hd not in result:
            result[hd] = node.info
        
    #   Enqueue the left child of the dequeued node if it exists 
        Q.append((node.left, hd-1))
       
    #   Enqueue the right child of the dequeued node if it exists.
        Q.append((node.right, hd+1))
        
    # Sort based on keys
    for i in sorted(result.keys()):
        # print the value separated by a space
        print(result[i], end=" ")
      


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)