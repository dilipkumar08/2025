#stack using linked list

class node():
  def __init__(self,data):
    self.data=data
    self.next=None

class Stack():
  def __init__(self):
    self.stack=None
    self.size=0

  def push(self,val):
    self.size+=1
    if not self.stack:
      self.stack=node(val)
    else:
      new_node=node(val)
      new_node.next=self.stack
      self.stack=new_node
    print(val,"pushed")
  def pop(self): 
    print(self.stack.data,"popped")
    self.stack=self.stack.next
    self.size-=1
    return


  def peek(self):
    if self.stack:
      print("peeking..",self.stack.data)
    else:
      print("Stack Empty")
  
  def display(self):
    if not self.stack:
      print("Stack Empty")
    else:
      print("Stack:")  
      current=self.stack
      
      while current:
        print(current.data)
        current=current.next
  def Size(self):
    print("Size of the stack",self.size)


if __name__=="__main__":
  s1=Stack()
  s1.push(1)
  s1.push(2)
  s1.push(3)
  s1.pop()
  s1.peek()
  s1.push(10)
  s1.push(8)
  s1.push(5)
  s1.push(6)
  s1.push(7)
  s1.display()
  s1.Size()
