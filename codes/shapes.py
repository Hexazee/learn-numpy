import numpy as np

# matrix 2x3
x = np.array((
        [3, 2, 1],
        [-4,-5,-2]
))

# Transpose
print(x)
y = np.transpose(x)
print(f'after being transposed: \n{y}\n')

# changes to rows vector / flatten array
print(x)
z = np.ravel(x)
print(f'after changes to rows vector: \n{z}\n')

# reshape
print(x)
a = x.reshape(3,2)
print(f'after to reshape: \n{a}\n')

# resize
print(x)
x.resize(6,1)
print(f'after to resize: \n{x}\n')