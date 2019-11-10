def successorBST(node):
  cur = node.right if node.right else None
  if cur:
    while cur.left:
      cur = cur.left
  else:
    cur = node.parent
    chi = node
    while cur and cur.right == chi:
      cur = cur.parent
      chi = cur

  return cur
