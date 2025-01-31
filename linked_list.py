class Node:
    def __init__(self, data = None, next=None):
        self.data = data
        self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    node = Node(data, self.head)
    self.head = node

  def insert_at_end(self, data):
    node = Node(data, None)
    if self.head is None:
      self.head = node
      return
    
    current = self.head
    while current.next:
      current = current.next
    
    current.next = node
      
  def insert_values(self, data_list):
    self.head = None
    for data in data_list:
      self.insert_at_end(data)
  
  def size(self):
    count = 0
    current = self.head
    while current:
      current = current.next
      count += 1

    return count

  def remove_at(self, index):
    if index < 0 or index >= self.size():
      raise Exception("Invalid index")
    
    # Remove at the beginning of the list
    if index == 0:
      self.head = self.head.next
      return

    count = 0
    itr = self.head
    while itr:
      if(count == index - 1):
        itr.next = itr.next.next
        break
      itr = itr.next
      count += 1
      
  def insert_at(self, index, data):
    node = Node(data, None)
    if index < 0 or index >= self.size():
      raise Exception("Invalid index")

    # Insert at the beginning of the list
    if(index == 0):
      return self.insert_at_beginning(data)

    itr = self.head
    count = 0
    while itr:
      if(count == index - 1):
        node = Node(data, itr.next)
        itr.next = node
        break

      count += 1
      itr = itr.next
    
  def search(self, data):
    if not self.head:
      return None
    
    if self.head.data == data:
      return True


    found = False
    itr = self.head
    while not found and itr:
      if itr.data == data:
        found = True
        break
      itr = itr.next
      

    return found

  def insert_after_value(self, value, data):
    if not self.head:
      return False
    
    if not data:
      return False
    
    itr = self.head
    while itr:
      if itr.data == value:
        node = Node(data, itr.next.next)
        itr.next = node
        break
      itr = itr.next
    
  def print(self):
    if self.head is None:
      print("Linked list is empty")
      return
    
    itr = self.head
    listr = ''

    while itr:
      listr += str(itr.data) + '-->'
      itr = itr.next
    
    print(listr)

    
if __name__ == '__main__':
  list = LinkedList()
  list.insert_values([1,2,3,4,5])
  list.remove_at(2)

  list.print()

  print("Before insertion")
  list.print()
  print("After insertion")
  list.insert_at(2, 3)
  list.print()

  print("After insertion after value")
  list.insert_at(2, 7)
  list.print()


  # search for first occurrence of data
  search = list.search(7)
  print(f"List has value? {search}")

  print(f'size {list.size()}')