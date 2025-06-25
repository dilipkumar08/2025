class Node():
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None

class Tree():
  def __init__(self):
    self.root= None
    self.size=0


  def insert(self,data):
    if not self.root:
      self.root=Node(data)
      self.size+=1
    else:
      queue=[self.root]
      while queue:
        temp=queue.pop(0)
        if not temp.left:
          temp.left=Node(data)
          self.size+=1
          break
        else:
          queue.append(temp.left)
        if not temp.right:
          temp.right=Node(data)
          self.size+=1
          break
        else:
          queue.append(temp.right)
    print("inserted ",data)

  def levelOrder(self):
    if not self.root:
      print("Empty")

    else:
      queue=[self.root]
      while queue:
        temp=queue.pop(0)
        print(temp.data,end=' ')
        if temp.left:
          queue.append(temp.left)
        if temp.right:
          queue.append(temp.right)

  def preOrder(self,node):
    if node:
      print(node.data,end=" ")
      self.preOrder(node.left)
      self.preOrder(node.right)
    
  def postOrder(self,node):
    if node:
      self.postOrder(node.left)
      self.postOrder(node.right)
      print(node.data,end=" ")
      
  def inOrder(self,node):
    if node:
      self.inOrder(node.left)
      print(node.data,end=" ")
      self.inOrder(node.right)

  def height(self,node):
    if not node:
      return 0
    right=self.height(node.right)
    left=self.height(node.left)
    return max(right,left)+1
  
  def Size(self):
    print("Size of the tree:",self.size)

if __name__=="__main__":
  t1=Tree()
  t1.insert(1)
  t1.insert(3)
  t1.insert(4)
  t1.insert(5)
  t1.insert(8)
  t1.insert(9)
  print("\nPost Order:")
  t1.postOrder(t1.root)
  print("\nPre Order:")
  t1.preOrder(t1.root)
  print("\nIn Order")
  t1.inOrder(t1.root)
  print("\nLevel Order")
  t1.levelOrder()
  print("\nHeight of the tree:",t1.height(t1.root))
  t1.Size()
  

