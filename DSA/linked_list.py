class node():
  def __init__(self,data):
    self.data=data
    self.next=None

class LinkedList():
  def __init__(self):
    self.head=None
  
  def append(self,val):
    if not self.head:
      self.head=node(val)
      return "inserted"
    last=self.head
    while last.next:
      last=last.next
    last.next=node(val)
    return "inserted"
  
  def print_list(self):
    current=self.head

    while current:
      print(current.data,end='->')
      current=current.next
    
  
  def delete(self,val):
    current =self.head
    if current.data==val:
      self.head=current.next
      return "deleted"
      current=None
    
    while current and current.data!=val:
      prev=current
      current=current.next

    if not current:
      print("Value is not present")
      return 
    else:
      prev.next=current.next
      return "deleted"

  def search(self,val):
    current=self.head
    index=0
    while current:
      if current.data==val:
        return index
      index+=1
    return "not exists"
  
  def prepend(self,val):
    first=node(val)
    first.next=self.head
    self.head=first

  def length(self):
    current=self.head
    n=0
    while current:
      n+=1
      current=current.next
    return n

  def sort_list(self):
    n=self.length()
    for i in range(n):
      current=self.head
      for j in range(n-i):
        if current.next:
          if current.data>current.next.data: 
            current.data,current.next.data=current.next.data,current.data
          current=current.next
        else:
          break

    self.print_list()



if __name__=='__main__':
  l1=LinkedList()
  print(l1.append(8))
  l1.print_list()
  print("\nindex of 8:",l1.search(8))
  print(l1.delete(8))
  print(l1.prepend(7))
  l1.print_list()
  print(l1.append(4))
  print(l1.append(2))
  print(l1.append(7))
  print(l1.append(3))
  print(l1.append(1))
  l1.sort_list()

