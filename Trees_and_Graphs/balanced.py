def checkBalanced(root):
  isBalanced, _ = checkBalancedRec(root)
  return isBalanced

def checkBalancedRec(root):
  if not root:
    return True, 0
  
  isBalanced, lh = checkBalancedRec(root.left)
  if not isBalanced:
    return False,lh

  isBalanced, rh = checkBalancedRec(root.right)
  if not isBalanced:
    return False,rh

  if abs(lh-rh) <= 1:
    return True, max(lh,rh)+1
  else:
    return False, lh
