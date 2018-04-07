class Node:
    def __init__(self,val):
        self.value = val
        self.leftChild = None
        self.rightChild = None
    
    def insert(self,data):
        if self.value == data:
            return(False)
        elif self.value > data:
            if self.leftChild:
                return(self.leftChild.insert(data))
            else:
                self.leftChild = Node(data)
                return(True)
        else:
            if self.rightChild:
                return(self.rightChild.inset(data))
            else:
                self.leftChild = Node(data)
                return(True)
    
    def find(self,data):
        if (self.value==data):
            return(True)
        elif self.value < data:
            return(self.leftChild.find(data))
        else:
            if self.rightChild:
                return(self.rightChild.find(data))
            else:
                return(False)
                
    def preorder(self):
        if self:
            print(self.value)
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(self.value)
    
    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(self.value)
            if self.rightChild:
                self.rightChild.inorder()
            
class Tree:
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        if self.root:
            return(self.root.insert(data))
        else:
            self.root = Node(data)
            return(True)    
    
    def find(self,data):
        if self.root:
            return(self.root.find(data))
        else:
            return(False)
            
    def preorder(self):
        print('PreOrder Traversal')
        self.root.preorder()
        
    def postorder(self):
        print('PostOrder Traversal')
        self.root.postorder()
        
    def inorder(self):
        print('InOrder Traversal')
        self.root.inorder()
        
