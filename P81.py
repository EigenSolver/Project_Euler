import numpy as np

with open('p081_matrix.txt') as f:
# with open('test.txt') as f:
    matrix = np.array([list(map(int, string.strip().split(',')))
                       for string in f.readlines()])
    print(matrix)

def greedy_sum(matrix):
    m = len(matrix)
    i, j = 0, 0
    count = matrix[i, j]
    while i + 1 < m and j + 1 < m:
        if matrix[i, j + 1] >= matrix[i + 1, j]:
            i += 1
        else:
            j += 1
        print(matrix[i,j])
        count += matrix[i, j]
    if i>j:
        while j<m-1:
            j+=1
            count += matrix[i, j]
    else:
        while i<m-1:
            i+=1
            count += matrix[i, j]
    print(i,j)
    return count

def recurive_sum(matrix):
    n, m = len(matrix), len(matrix[0,:])
    for i in range(n):
        for j in range(m):
            matrix[i,j]+=min(matrix[i-1,j],matrix[i,j-1]) if i*j>0 else (matrix[i-1,j] if i else (matrix[i,j-1] if j else 0))

print(recurive_sum(matrix))
