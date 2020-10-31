import numpy as np

# Create Matrix 3x3
matrix = np.array([
    (1,2,3),
    (4,5,6),
    (-1,-2,-3)
])

print(matrix)

# Manipulasi menggunakan SKALAR
print(f'Ditambah 4 \n {matrix + 4}')
print(f'Dikali 2 \n {matrix * 2}')      
print(f'Dikurang 5 \n {matrix - 5}')
print(f'Dibagi 2 \n {matrix / 2}')


'''
 Tidak berlaku perkalian Matriks, karena numpy menggunakan "elementwise operation"
'''