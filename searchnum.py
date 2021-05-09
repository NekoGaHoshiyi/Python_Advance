
def findinMatrx(Matrix, num):
    i = len(Matrix) - 1
    j = len(Matrix[0]) - 1
    while i >= 0 and j >= 0:
        # if i == 0 and j == 0 and Matrix[0][0] != num:
        #     break
        if i > len(Matrix) - 1:
            break
        if Matrix[i][j] > num:
            if i > 0:
                i -= 1
            if j > 0:
                j -= 1
            elif j == 0:
                break
        if Matrix[i][j] == num:
            return (i+1, j+1)
        if Matrix[i][j] < num:
            i += 1
    return -1


matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

print(findinMatrx(matrix, 1))
print(findinMatrx(matrix, -1))
print(findinMatrx(matrix, 31))

