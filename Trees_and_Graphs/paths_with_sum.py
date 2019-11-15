def path_with_sum(root, targetSum):
  if not root:
    return 0

  count = [0]
  paths_with_sum_count(root, targetSum, count)

  return count[0] + path_with_sum(root.left, targetSum) + path_with_sum(root.right, targetSum)

def paths_with_sum_count(root, targetSum, count):
  if not root:
    return

  if root.val == targetSum:
    count[0] += 1

  paths_with_sum_count(root.left, targetSum - root.val, count)
  paths_with_sum_count(root.right, targetSum - root.val, count)

def path_with_sum_optimum(root, targetSum):
  
  count = [0]
  runningSum = 0
  d = defaultdict(int)

  paths_with_sum_optimum_rec(root, targetSum, runningSum, d, count)
  return count[0]

def paths_with_sum_optimum_rec(root, targetSum, runningSum, d, count)
 if not root:
   return

 runningSum += root.val
 d[runningSum] += 1
 if (runningSum - targetSum) in d:
   count[0] += d[runningSum - targetSum]


 paths_with_sum_optimum_rec(root.left, targetSum, runningSum, d, count)
 paths_with_sum_optimum_rec(root.left, targetSum, runningSum, d, count)

 d[runningSum] -= 1
