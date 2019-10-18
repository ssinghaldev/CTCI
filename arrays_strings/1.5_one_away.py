def one_away(str1, str2):
  len1 = len(str1)
  len2 = len(str2)

  if abs(len1 - len2) >= 2:
    return False

  if len1 == len2:
    num_changes = 0
    for c1, c2 in  zip(str1, str2):
      if c1 != c2:
        num_changes += 1
    
    if num_changes > 1:
      return False
  else:
    s1, s2 = (str2, str1) if len1 < len2 else (str1,str2)

    i = 0
    j = 0
    num_changes = 0
    while i < len(s1):
      if j == len(s2):
        break
      elif s1[i] != s2[j] and num_changes:
        return False
      elif s1[i] != s2[j] and not num_changes:
        num_changes = 1
        i += 1
      else:
        i += 1
        j += 1      
    
  return True

print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))
  
