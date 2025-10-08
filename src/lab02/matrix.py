def transpose(mat):
    if len (mat) == 0:
        return []
    row_length = len(mat[0])
    if any(len(row) != row_length for row in mat):
        return "ValueError"
    return list(map(list, zip(*mat)))


def row_sums(mat):
    if len(mat) == 0:
        return []
    row_length = len(mat[0])
    if any(len(row) != row_length for row in mat):
        return "ValueError"
    return [sum(row) for row in mat]


def col_sums(mat):
    if len(mat) == 0:
        return []
    row_length = len(mat[0])
    if any(len(row) != row_length for row in mat):
        return "ValueError"
    return [sum(col) for col in list(zip(*mat))]

print('transpose:')
print(transpose([ [1, 2, 3] ]), transpose([ [1], [2], [3] ]), transpose([ [1, 2], [3, 4] ]), sep = '\n')
print(transpose([]), transpose([[1, 2], [3]]), sep = '\n')
print('row_sums:')
print(row_sums([ [1, 2, 3], [4, 5, 6] ]), row_sums([[-1, 1], [10, -10]]), sep = '\n')
print(row_sums([[0, 0], [0, 0]]), row_sums([[1, 2], [3]]), sep = '\n')
print('col_sums:')
print(col_sums([ [1, 2, 3], [4, 5, 6] ]), col_sums([[-1, 1], [10, -10]]), sep = '\n')
print(col_sums([[0, 0], [0, 0]]), col_sums([[1, 2], [3]]), sep = '\n')