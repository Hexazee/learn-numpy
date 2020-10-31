import numpy as np 

# Create Vectors
vector1 = np.array([1, 2, 3, 4, 5])
vector2 = np.arange(1, 10, 2)
vector3 = np.linspace(1, 10, 4)
vector4 = np.zeros(5)

# Create Matrix
matrix1 = np.array([
		(1, 2, 3),
		(4, 5, 6)
	])

# Create Matrix (value 0)
matrix2 = np.zeros((3,2))	# Ordo -> 3x2
matrix3 = np.zeros((3,3))	# Ordo -> 3x3

# Create Matrix (value 1)
matrix2 = np.ones((3,2))	# Ordo -> 3x2
matrix3 = np.ones((3,3))	# Ordo -> 3x3

matrix4 = np.identity(5)	# Ordo -> 5x5
matrix5 = np.eye(5)			# == identity

# Show on Console
print(vector2)


# Indexcing
for index,item in enumerate(vector2):
	print(f'Index {index} -> element {item}')

# Slacing
print(f'Element 1-3 -> {vector2[:3]}')
print(f'Element 3-5 -> {vector2[2:]}')
