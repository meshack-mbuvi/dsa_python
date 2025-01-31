class HashTable:
  def __init__(self):
    self.MAX = 100
    self.arr = [[] for i in range(self.MAX)]

  def get_hash(self, key):
    h = 0
    for char in key:
      h += ord(char)

    return h % self.MAX

  def __setitem__(self, key, value):
    h = self.get_hash(key)
    
    found = False
    for idx, element in enumerate(self.arr[h]):
      if len(element) == 2 and element[0] == key:
        self.arr[h][idx] = (key, value)
        found = True
        break

    if not found:
      self.arr[h].append((key, value))

  def __getitem__(self, key):
    h = self.get_hash(key)
    return self.arr[h]


t = HashTable()
t['march 6'] = 130
t['march 6'] = 78
t['march 8'] = 67
t['march 9'] = 4
t['march 17'] = 459

print(t['march 17'])
print(t['march 6'])