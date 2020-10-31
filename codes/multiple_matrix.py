import numpy as np  

# Matrix 3x3 
matrix = np.array((
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ))

# Matrix Identity
matrix_2 = np.identity(3)

# Multiple Matrix
result = np.dot(matrix,matrix_2)

print(f'Result from: \n{matrix} \n{matrix_2} \n-----------\n {result}')
