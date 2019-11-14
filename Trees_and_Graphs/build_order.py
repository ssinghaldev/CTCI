from collections import defaultdict

def build_order(projects, dependencies):
  g = defaultdict(list)
  for project in projects:
    g[project] = []

  for f,s in dependencies:
    if f in g:
      g[f].append(s)

  buildOrder = []
  visited = set()
  for node in g:
    if node not in visited:
      findBuildOrder(g, node, buildOrder, visited)

  while buildOrder:
    print(buildOrder.pop())

def findBuildOrder(g, n, buildOrder, visited):

  visited.add(n)
  for c in g[n]:
    if c not in visited:
      findBuildOrder(g,c, buildOrder,visited)

  buildOrder.append(n)

build_order(['a', 'b', 'c', 'd', 'e', 'f'], 
            [('a', 'b'), ('f', 'b'), ('b','d'), ('f', 'a'), ('d', 'c')])
