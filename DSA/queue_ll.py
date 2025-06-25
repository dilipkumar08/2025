class node():
  def __init__(self,data):
    self.data=data
    self.next=None
class Queue():
  def __init__(self):
    self.queue=None
    self.size=0
  
  def enqueue(self,val):
    if not self.queue:
      self.queue=node(val)
    else:
      current=self.queue
      while current.next:
        current=current.next 
      current.next=node(val)
    print(val,"enqueued")
    self.size+=1

  def dequeue(self):
    if not self.queue:
      print("Queue is Empty")
    else:
      print(self.queue.data,"dequeued")
      self.queue=self.queue.next
      self.size-=1

  def display(self):
    if not self.queue:
      print("Queue is Empty")
    else:
      current=self.queue
      print("Queue")
      while current:
        print(current.data)
        current=current.next

  def peek(self):
    if not self.queue:
      print("Queue is Empty")
    else:
      print("peeking...",self.queue.data)

  def Size(self):
    print("The size of the queue is",self.size)


if __name__=="__main__":
  q1=Queue()
  q1.enqueue(1)
  q1.dequeue()
  q1.display()
  q1.dequeue()
  q1.Size()
  q1.enqueue(2)
  q1.enqueue(8)
  q1.enqueue(12)
  q1.enqueue(15)
  q1.display()
  q1.peek()
