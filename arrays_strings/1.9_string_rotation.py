# is s1 a substring of s2
def isSubstring(s1, s2):
    pass
   
# Is s2 a rotation of s1
def isStringRotated(s1,s2):
    s = s2 + s2
    return isSubstring(s1,s)

