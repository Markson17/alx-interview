# 0x07-rotate_2d_matrix

This repository contains a Python script that implements a function to rotate a given n x n 2D matrix by 90 degrees clockwise. The matrix is rotated in-place, and the function is designed to modify the matrix directly without returning anything.

## Task Description

The goal of this task is to take an n x n 2D matrix as input and rotate it by 90 degrees clockwise. The rotation should be performed in-place, meaning the matrix should be modified directly without creating a new matrix.

## Function Prototype

```python
def rotate_2d_matrix(matrix):
    """
    Rotates the given n x n 2D matrix 90 degrees clockwise in-place.
    
    :param matrix: The n x n 2D matrix to be rotated.
    :type matrix: list[list[int]]
    """
```

## Usage

To use the provided function, follow these steps:

1. Import the `rotate_2d_matrix` function from the module:

```python
from 0-rotate_2d_matrix import rotate_2d_matrix
```

2. Create a 2D matrix that you want to rotate. The matrix should be represented as a list of lists, where each inner list corresponds to a row in the matrix.

```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
```

3. Call the `rotate_2d_matrix` function and pass the matrix as an argument:

```python
rotate_2d_matrix(matrix)
```

4. After calling the function, the matrix will be rotated 90 degrees clockwise in-place.

5. You can print the rotated matrix to see the result:

```python
print(matrix)
```

## Example

```python
from 0-rotate_2d_matrix import rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
```

Expected output:

```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

