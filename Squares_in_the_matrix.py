def is_square(matrix, i, j, k, l):
    for a in range(i, k+1):
        for b in range(j, l+1):
            if matrix[a][b] == 0:
                return False
    return True

def find_squares(matrix):
    #Returns the number of squares formed by 1's in the matrix
    
    if len(matrix) <2 or len(matrix[0]) < 2:
        return 0
    
    num_of_sqs = 0
    for i in range(len(matrix)-1):
        if 1 not in matrix[i]:
            continue
        for j in range(len(matrix[0])-1):
            if matrix[i][j] == 1:
                k, l = i+1, j+1
                while(k < len(matrix) and l < len(matrix[0])):
                    if is_square(matrix, i, j, k, l):
                        num_of_sqs += 1
                    k += 1
                    l += 1
    return num_of_sqs
    
matrix = [[1, 1, 1], [1, 1, 0], [1, 1, 1]]

print(find_squares(matrix))
