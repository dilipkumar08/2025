#queue

class Queue():
  def __init__(self):
    self.queue=[]
    self.size=0

  def enqueue(self,val):
    self.queue.append(val)
    print(val,"enqueued")
    self.size+=1
  
  def dequeue(self):
    if self.queue:
      print(self.queue.pop(),"dequeued")
      self.size-=1
    else:
      print("Queue is empty")
  
  def peek(self):
    print("peeking..",self.queue[-1]) if self.queue else print("Queue is empty")

  def display(self):
    if self.queue:
      print("Queue")
      for i in self.queue:
        print(i)
    else:
      print("Queue is empty")

if __name__=="__main__":
  q1=Queue()
  q1.enqueue(2)
  q1.dequeue()
  q1.enqueue(3)
  q1.dequeue()
  q1.display()
  q1.dequeue()
  q1.enqueue(2)
  q1.enqueue(5)
  q1.enqueue(7)
  q1.enqueue(8)
  q1.enqueue(9)
  q1.enqueue(10)
  q1.peek()
  q1.display()
        
  
