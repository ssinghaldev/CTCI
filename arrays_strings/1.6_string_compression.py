def compressString(s): 
  if s == "": 
    return "" 
  
  cs = [] 
  count = 1 
  for idx in range(len(s)): 
    if idx == 1: 
      continue 
    if s[idx] == s[idx - 1]: 
      count += 1 
    else: 
      cs.append(s[idx-1]) 
      cs.append(str(count)) 
      count = 1 

  cs.append(s[-1]) 
  cs.append(str(count))

  compressedStr = ''.join(cs) 
  if len(compressedStr) < len(s): 
    return compressedStr 
  else:
    return s
