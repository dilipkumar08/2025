#stack
class Stack():
  def __init__(self):
    self.stack=[]

  def push(self,val):
    self.stack.append(val)
    print(val,"pushed")
  def pop(self):
    print(self.stack.pop(0),"popped")
  
  def peek(self):
    if self.stack:
      print("peeking..",self.stack[-1])
    else:
      print("stack is empty")
    
  def display(self):
    if self.stack:
      print("stack:")
      for i in self.stack[::-1]:
        print(i)
    else:
      print("stack is empty")
  
  def size(self):
    print("size of the stack:",len(self.stack))

if __name__=="__main__":
  s1=Stack()
  s1.push(1)
  s1.push(2)
  s1.push(3)
  s1.pop()
  s1.peek()
  s1.display()
  s1.push(4)
  s1.push(7)
  s1.display()
  s1.size()

  
