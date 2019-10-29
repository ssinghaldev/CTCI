def zeroMatrix(m):
    
    rows = len(m)
    cols = len(m[0])
    
    firstRowHasZero = 0
    firstColHasZero = 0
    
    for col in range(cols):
        if m[0][col] == 0:
            firstRowHasZero = 1
            break
    
    for row in range(rows):
    if m[row][0] == 0:
        firstColHasZero = 1
        break

    for row in range(1, rows):
        for col in range(1, cols):
        if m[row][col] == 0:
            m[0][col] = 0
            m[row][0] = 0
    
    for row in range(1, rows):
        if m[row][0] == 0:
            for col in range(cols):
                m[row][col] = 0
    
    for col in range(1, cols):
    if m[0][col] == 0:
        for row in range(rows):
            m[row][col] = 0
   
   if firstRowHasZero:
       for col in range(cols):
           m[0][col] = 0
   
   if firstColHasZero:
       for row in range(rows):
           m[row][0] = 0 
   
    return m
