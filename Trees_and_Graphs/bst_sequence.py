from collections import deque

def bst_sequence(root):
  results = []

  if root == None:
    results.append([])
    return results

  left_lists = bst_sequence(root.left)
  right_lists = bst_sequence(root.right)

  for left_list in left_lists:
    for right_list in right_lists:
      new_lists = combine(left_list, right_list, [root.val])
      results.extend(new_lists)

  return results


def combine(l1, l2, prefix):
  results = []

  if not l1:
    results.append(prefix + l2)
    return results

  if not l2:
    results.append(prefix + l1)
    return results
 
  // Taking first ele of l1
  e1 = l1.pop(0)
  prefix.append(e1)

  r1 = combine(l1, l2, prefix)

  prefix.pop()
  l1.insert(0,e1)
  
  // Taking first ele of l2
  e2 = l2.pop(0)
  prefix.append(e2)

  r2 = combine(l1, l2, prefix)

  prefix.pop()
  l2.insert(0, e2)

  results.extend(r1)
  results.extend(r2)

  return results
