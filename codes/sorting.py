import numpy as np 

######## CASE 1 #########
# data_tipe = [('nama','S30'), ('tinggi',int)]
# data = [
# 		('Danang', 165), 
# 		('Hapis', 155), 
# 		('Fadillah', 170)
# 	]

# x = np.array(data, dtype=data_tipe)

# print(x, '\n')

# # Sorting berdasarkan Nama
# print(f'----SORT NAME----\n {np.sort(x, order="nama")}')
# # Sorting berdasarkan tinggi badan
# print(f'----SORT HEIGHT BODY----\n {np.sort(x, order="tinggi")}')

######## CASE 2 ##########
# a = np.floor(np.random.randn(3,4)**2)
# print(a)

# print(f'Nilai max dari matriks a : {np.max(a)}')
# print(f'Posisi nilai max a : {np.argmax(a)}')
# print(f'Nilai min dari matriks a : {np.min(a)}')
# print(f'Posisi nilai min a : {np.argmin(a)}')

######## CASE 3 ##########
# x = np.floor(np.random.randn(3,3)**2)
# y = np.round(np.random.randn(3,2)**3)

# z = x.dot(y)
# print(f'Hasil dari Perkalian Matriks: \n{x}\n& & & & & & &\n{y}')
# print('______________\n',z)