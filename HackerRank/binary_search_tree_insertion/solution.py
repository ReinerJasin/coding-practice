class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    # Create new function that allows us to pass the current node without starting from root
    def recurring_insert(self, node, val):
        # If the code enter this function, it means the root is not None
        # Check if val < current node value (meaning it suppose to go left)
        if val < node.info:
            # Check if there's existing node on the left
            if node.left != None:
                # If there is node, we just re run the insert using the current node to check it's left and right
                self.recurring_insert(node.left, val)
            else:
                # If empty, then insert to the left of this leaf
                node.left = Node(val)
        
        # Same function goes to the right side of the node
        else:
            if node.right != None:
                self.recurring_insert(node.right, val) 
            else:
                node.right = Node(val)
        
    def insert(self, val):
        #Enter you code here.
        # Set root node if none exist
        if self.root == None:
            self.root = Node(val)
        # Start the recurring searching if root already exist
        else:
            self.recurring_insert(self.root, val)
            
        # Return the result root
        return self.root

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
