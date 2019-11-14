def first_common_ancestor(root, node1, node2):
  return first_common_ancestor_rec(root, node1, node2)

def first_common_ancestor_rec(root, node1, node2):
  if not root:
    return None,0

  if node1 == root and node2 == root:
    return root, 2
  
  lca_left,num_nodes_left = first_common_ancestor(root.left, node1, node2)
  lca_right,num_nodes_right = first_common_ancestor(root.right, node1, node2)

  if lca_left and lca_right:
    return root,2

  if lca_left and num_nodes_left == 2:
    return lca_left,2
      
  if lca_right and num_nodes_right == 2:
    return lca_right,2 

  if (root == node1 || root == node2) and (lca_left || lca_right):
    return root,2
  
  if left_lca != None
    return left_lca, 1
  elif right_lca != None
    return right_lca, 1

  return None, 0
