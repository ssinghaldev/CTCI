import random

class Tree:
  def __init__(self, root=None):
    self.root = root

  def insertNode(self, treeNodeKey):
    if not self.root:
      self.root = TreeNode(treeNodeKey)
    else:
      self.root.insertNode(treeNodeKey)

  def deleteNode(self, treeNodeKey):
    pass

  def findNode(self, treeNodeKey):
    
    if self.root:
      return self.root.findNode(treeNodeKey)
    return None

  def getRandomNode(self):
    s = self.root.size
    idx = random.randrange(size)
    return self.root.getIdxNode(idx)

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.size = 1
  
  def getIdxNode(self, idx):
    left_size = 0
    if self.left:
      left_size = self.left.size

    if idx < left_size:
      return self.left.getIdxNode(idx)
    elif idx == left_size:
      return self
    else:
      return self.right.getIdxNode(idx - (left_size + 1))

  def insertNode(self, treeNodeKey):
    if self.val < treeNodeKey:
      if self.right:
        self.right.insertNode(treeNodeKey)
      else:
        self.right = TreeNode(treeNodeKey)
    else:
      if self.left:
        self.left.insertNode(treeNodeKey)
      else:
        self.left = TreeNode(treeNodeKey)

  def findNode(self, treeNodeKey):
    if self..val == treeNodeKey:
      return self
    else if self.val < treeNodeKey:
      return self.right ? self.right.findNode(treeNodeKey): self.right
    else:  
      return self.left ? self.left.findNode(treeNodeKey) : self.left 

