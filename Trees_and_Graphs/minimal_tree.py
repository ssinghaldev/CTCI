def minimalTree(arr):
 
 if len(arr) == 1:
   return node(arr[0])

 idx = len(arr) // 2
 n  = node(arr[idx])
 n.left = minimalTree(arr[:idx])
 n.right = minimalTree(arr[idx:])

 return n
