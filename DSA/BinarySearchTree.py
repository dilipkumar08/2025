class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinarySearchTree():
    def __init__(self):
        self.root=None
        self.size=0
    
    def insert(self,val:int):
        self.root,status=self.insert_recursive(self.root,val,"inserted")
        if status=='inserted':
            self.size+=1
        print(val,status)
    
    def insert_recursive(self,root: Node,val: int,status: str):
        if not root:
            return Node(val),status
        
        else:
            if root.data>val:
                root.left,status=self.insert_recursive(root.left,val,status)
            elif root.data<val:
                root.right,status=self.insert_recursive(root.right,val,status)
            else:
                return root,"already exists"
            
            return root,status
    
    def delete(self,val):
        self.root,status=self.delete_recursive(self.root,val,"deleted")
        if status=="deleted":
            self.size-=1
        print(val,status)

    def delete_recursive(self,root:Node,val:int,status:str):
        if not root:
            return root, "not exists"
        else:
            if root.data>val:
                root.left,status=self.delete_recursive(root.left,val,status)
            elif root.data<val:
                root.right,status=self.delete_recursive(root.right,val,status)
            else:
                if not root.left:
                    return root.right,status
                elif not root.right:
                    return root.left,status
                else:
                    root.data=self.min_inorder(root.right).data
                    root.right,status=self.delete_recursive(root.right,root.data,status)


            return root,status
    
    def find(self,val):
        status=self.find_recursive(self.root,val,"found")
        print(val,status)

    def find_recursive(self,root: Node,val:int,status:str):
        if not root:
            return "not found"
        else:
            if root.data>val:
                return self.find_recursive(root.left,val,status)
            elif root.data<val:
                return self.find_recursive(root.right,val,status)
            else:
                return status
            
    def height(self,root):
        if not root:
            return 0
        right=self.height(root.right)
        left=self.height(root.left)
        return max(right,left)+1


    def min_inorder(self,root):
        while root.left:
            root=root.left
        return root
    
    def inOrder(self,root):
        if root:
            self.inOrder(root.left)
            print(root.data,end=" ")
            self.inOrder(root.right)



if __name__=="__main__":
    b1=BinarySearchTree()
    b1.insert(19)
    b1.insert(10)
    b1.insert(12)
    b1.insert(9)
    b1.insert(5)
    b1.insert(10)
    b1.insert(8)
    b1.insert(3)
    b1.insert(15)

    b1.inOrder(b1.root)
    b1.delete(12)
    b1.inOrder(b1.root)
    b1.find(15)
    b1.find(12)
    b1.height(b1.root)
    
