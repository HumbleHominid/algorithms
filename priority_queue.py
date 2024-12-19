# Given index n return the parent index
def parent(n:int) -> int:
  if n == 0: return -1
  return (n-1)//2

def young_child(n:int) -> int:
  return 2*n+1

class priority_queue[T]:
  arr: list[T] = []

  def insert(self, val:T):
    # Will potentially cause a realloc
    self.arr.append(val)
    self.bubble_up(len(self.arr)-1)

  def bubble_up(self, n:int):
    # we are at the head node
    if parent(n) == -1:
      return
    if self.arr[parent(n)] > self.arr[n]:
      self.arr[parent(n)], self.arr[n] = self.arr[n], self.arr[parent(n)]
      self.bubble_up(parent(n))

  def bubble_down(self, n:int):
    c = young_child(n)
    min_index = n
    for i in [0, 1]:
      if c+i < self.size:
        if self.arr[min_index] > self.arr[c+i]:
          min_index = c+i

    if min_index != n:
      self.arr[min_index], self.arr[n] = self.arr[n], self.arr[min_index]
      self.bubble_down(min_index)
  
  def pop_min(self) -> T:
    min = self.arr[0]
    try:
      self.arr[0] = self.arr.pop()
      self.bubble_down(0)
    except: pass
    return min

  def print(self):
    print(*self.arr)
