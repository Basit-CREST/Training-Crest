def sum_of_diogonal(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                sum += matrix[i][j]
    return sum

list_matrix = [[ i*3 + j for j in range(3)] for  i in range(3)]
print(list_matrix)

print(sum_of_diogonal(list_matrix))