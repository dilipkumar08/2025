class Hash():
  def __init__(self,capacity=10):
    self.capacity=capacity
    self.size=0
    self.table=[[] for i in range(capacity)]

  def _hash(self,val):
    return hash(val)%self.capacity

  def add(self,val):
    index=self._hash(val)
    if val not in self.table[index]:
      self.table[index].append(val)
      print(val,"added")
      self.size+=1
    else:
      print(val,"already exists")

  def remove(self,val):
    index=self._hash(val)
    if val  in self.table[index]:
      self.table[index].remove(val)
      print(val,"removed")
      self.size-=1
    else:
      print(val,"not available")
    
  def format(self):
    if self.size!=0:
      li=[]
      for i in self.table:
        li.extend(i)
      print("{"+",".join(li)+"}")
    else:
      print("The hash is empty")

    

  def clear(self):
    self.table=[[]for i in range(self.capacity)]
    self.size=0

  def Size(self):
    print("size of the hash",self.size)

if __name__=="__main__":
  h1=Hash(20)
  h1.add("dilip")
  h1.add("kumar")
  h1.add("dilip")
  h1.remove("kumar")
  h1.add("me")
  h1.add("please")
  h1.add("help")
  h1.format()
  h1.Size()
  h1.clear()
  h1.format()
