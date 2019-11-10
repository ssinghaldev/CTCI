def validateBST(root):
  '''
  This ain't correct. This seems so simple but it is a very good trick
  question. Kudos! 
  cond_1 = (root.left and root.left.val <= root.val) or (not root.left)
  cond_2 = (root.right and root.right.val > root.val) or (not root.right)

  if cond_1 and cond_2:
    return validateBST(root.left) and validateBST(root.right)
  '''

  return validateBSTCorrect(root, None, None)

def validateBSTCorrect(root, mi, ma):
  if not root:
    return True

  if (ma and not root.val < ma) or not validateBSTCorrect(root.left, mi, root.val):
    return False

  if (mi and not root.val >= mi) or not validateBSTCorrect(root.right, root.val, ma):
    return False

  return True
