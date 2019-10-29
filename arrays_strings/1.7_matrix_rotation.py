def rotate_matrix(matrix):
  if len(matrix) == 0:
    return matrix

  n = len(matrix[0])

  for layer in range(n // 2):
    start = layer
    end   = n - 1 - layer

    common_axis = layer
    for i in range(start, end):
      top = matrix[common_axis][i]

      matrix[common_axis][i] = matrix[n-1-i][common_axis]

      matrix[n-1-i][common_axis] = matrix[n-1-common_axis][n-1-i]

      matrix[n-1-common_axis][n-1-i] = matrix[i][n-1-common_axis]

      matrix[i][n-1-common_axis] = top


  return

matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
rotate_matrix(matrix)

print(matrix)
