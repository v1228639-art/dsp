class BST:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.root=value
        
    def insert(self,data):
        if self.root:
            if data<self.root:
                if self.left is None:
                    self.left=BST(data)
                else:
                    self.left.insert(data)
            elif data>self.root:
                if self.right is None:
                    self.right=BST(data)
                else:
                    self.right.insert(data)
        else:
            self.root=data
            
    def preorder():
        print(self.root,end="")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
root=BST(10)
print("root:",10)
list=[10,20,30,40,15,6]
print("Given the list is:",list)
for i in list:
    root.insert(i)
print("Pre-Order Travesal")
root.preorder()
print()
