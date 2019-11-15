def checkSubTree(r1, r2):
  if not r1 and not r2: 
    return True

  if not r1: 
    return False

  if not r2:
    return True

  if checkTreeValues(r1, r2):
    return True

  return (checkSubTree(r1.left, r2) || checkSubTree(r1.right, r2))

def checkTreeValues(r1, r2):
  if not r1 and not r2:
    return True

  if not r1 or not r2:
    return False

  if r1.val != r2.val:
    return False

  return checkTreeValues(r1.left, r2.left) and checkTreeValues(r1.right, r2.right)
