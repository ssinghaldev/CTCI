from collections import deque

def listDepths(root):
  d = deque()
  d.append((root, 1))

  lists = []

  while d:
    n, level = d.popleft()
    if len(lists) < level:
      lists.append([n])
    else:
      lists[level-1].append(n)

    d.append(n.left, level+1)
    d.append(n.right, level+1)

  return lists
