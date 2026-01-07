# Initializing Arrays


## Create a 2×3 matrix identical to [[1, 2, 3], [4, 5, 6]]
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr.shape)

## Create an array of size n with each value equal to m
n = 5
m = 7

arr = np.full(n, m)
print(arr)

## Create a random array of dimensions 4×3×4
RANDOM_ARR = np.random.rand(4, 3, 4)
print(RANDOM_ARR)

## Create an identity matrix of size n × n
n = 3
EYE = np.eye(n)
print(EYE)

## Reshape / Transpose / Flatten
y = np.array([[1,2,3],
              [4,5,6]])
## Transpose using reshape
y_transpose = y.reshape(3,2)
print(y_transpose)
## Flatten using reshape
y_flattened = y.reshape(-1)
print(y_flattened)

## Skipping Dimension with -1
arr = np.random.randint(1,10,size=(4,5,7,3))
arr_new = arr.reshape(1, -1)
print(arr_new.shape)

## Create array of shape (3,4)
arr = np.arange(1,13).reshape(3,4)
print(arr)
print(arr.dtype)

## Linspace
start = 0.1
end = 0.9

arr = np.linspace(start, end, num=10)
print(arr)


# Slicing
arr1 = np.array([1,2,3,4,5])

print(arr1)
print(arr1[0:5])
print(arr1[0:4])
print(arr1[0:4:1])
print(arr1[0:4:2])
print(arr1[::-1])

## slicing of multi-dimensional arrays 
arr = np.arange(40).reshape(4,-1)
print(arr)
print(arr[1:4, 2:5])


# Copies vs References
arr = np.random.randint(10, size=6)
new_arr = arr
arr[0] = 100

print(arr)
print(new_arr)

## Proper copy
arr = np.random.randint(10, size=6)
new_arr = arr.copy()
arr[0] = -39

print(arr)
print(new_arr)


# Random Number Generation

## Random Number Generation in NumPy
arr = np.random.rand(3,4)
print(arr)

## Aggregation and Reduction Operations
np.random.seed(31)
arr = np.random.rand(3,4)
print(arr)

## Broadcasting and Element-wise Operations
arr = np.random.randint(5, 13, size=(2,4))
print(arr)

# Aggregation Functions
arr = np.arange(10).reshape(2,5)

print(arr.sum())
print(arr.mean())
print(arr.std())
print(arr.min())

## Multidimensional array 
arr = np.array([[1,2,9],
                [3,4,5],
                [-3,8,7]])

print(arr.max(axis=0))
print(arr.max(axis=1))
print(arr.max(), arr.min(), arr.mean())


# Broadcasting
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(arr1 * 2)
print(arr1 * arr2)

## Square each element
arr = np.random.randint(12, size=3)
arr_square = arr ** 2
print(arr_square)

## some more operators
import numpy as np

arr = np.arange(12).reshape(3,4)

print(arr)
print(arr + 1)    
print(arr - 1)    
print(arr * 2)     
print(arr / 2)     
print(arr // 2)    
print(arr ** 3)    

## Broadcasting with 1D array
arr1 = np.array([1, 2, 3, 4])
print(arr * arr1)

## Broadcasting with another 1D array
arr2 = np.array([7, 2, 5, 8])
print(arr2 * arr)

## Broadcasting with different shapes
arr1 = np.arange(12).reshape(3,4)
arr2 = np.arange(4)

print(arr1)
print(arr2)
print(arr1 + arr2)






