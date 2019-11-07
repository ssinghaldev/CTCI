
def route(a, b):
  l = []
  l.append(a)

  visited = {}
  while l:
    t = l.pop(0)
    visited[t] = 1

    for s in t.adjacent:
      if s == b:
        return True
      l.append(s)

  return False
