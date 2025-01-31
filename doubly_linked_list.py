# TODO: Implement doubly linked list
# TODO: Implement function to print_backward
# TODO: Implement function to print_forward
class Node:
  def __init__(self, data, prev, next):
    self.data = data
    self.prev = prev
    self.next = next

class DoublyLinkedList:
  def __init__(self):
    self.head = None

  def insert_values(self, data_list):
    self.head = None
    for data in data_list:
      self.insert_at_end(data)
    
  def insert_at_end(self, data):
    if self.head is None:
      self.head = Node(data, None, None)
      return

    itr = self.head
    while itr:
      if not itr.next:
        # add new node here
        node = Node(data, itr, None)
        itr.next = node
        break
      
      itr = itr.next

  def insert_at_beginning(self, data):
    node = Node(data, None, self.head)
    
    if self.head:
      self.head.prev = node
      self.head = node

    self.head = node

  def size(self):
    count = 0
    itr = self.head
    while itr:
      count += 1
      itr = itr.next

    return count
  
  def insert_at(self, index, data):
    if index < 0 or index >= self.size():
      raise Exception("Index out of range")

    if index == 0:
      return self.insert_at_beginning(data)

    itr = self.head
    count = 0
    while itr:
      if (count == index - 1):
        node = Node(data, itr, itr.next)
        itr.next = node
        break
      itr = itr.next

  def remove_at(self, index):
    if index < 0 or index >= self.size():
      raise Exception("Index out of range")
    
    
    if index == 0:
      self.head = None

    # find the node to remove
    itr = self.head
    count = 0
    while itr:
      if count == index:
        # point itr.prev node next to itr.next
        itr.prev.next = itr.next
        break
      count += 1
      itr = itr.next
      


  def print_forward(self):
    data = ''
    itr = self.head
    while itr:
      data += str(itr.data) + '-->'
      itr = itr.next
    
    print(data)

  def print_backward(self):
    # go to end of the list
    itr = self.head
    while itr.next:
      itr = itr.next

    # navigate backward printing the data
    data = ''
    while itr:
      data += str(itr.data) + '-->'
      itr = itr.prev

    print(data)

  
if __name__ == '__main__':
  list = DoublyLinkedList()
  list.insert_at_beginning("A")
  list.insert_at_beginning("B")
  list.print_forward()

  list.insert_values(["Apple", "Boy", "Cow"])
  list.print_forward()
  list.print_backward()
  list.insert_at(1, 'Girl')
  list.print_forward()

  # remove girl
  list.remove_at(1)
  list.print_forward()


  print(list.size())