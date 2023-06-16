class Node:
  def __init__(self, x) :
    self.key = x
    self.left = None
    self.right = None

  def altura(self, root):
    if root is None:
      return 0
  
    return max(self.altura(root.left), self.altura(root.right)) + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7) #Altura 3
# root.right.right.right = Node(10) #Altura 4 

print(root.altura(root))