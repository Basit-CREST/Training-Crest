matrix1 = [[ i*3 + j for j in range(1,4)] for i in range(3)]
matrix2 = [[ i*3 - j for j in range(3)] for i in range(3,0,-1)]

print(matrix1)
print(matrix2)


## using list comprehension
def matrix_mul(mat1,mat2):
    ans = [ [ sum(mat1[i][k]*mat2[k][j] for k in range(len(mat2))) for j in range(len(mat2[0]))]  for i in range(len(mat1))]
    return ans

print(matrix_mul(matrix1,matrix2))