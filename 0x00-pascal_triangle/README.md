# Pascal's Triangle

This module provides a function to generate Pascal's Triangle and a function to print the triangle.

## Functions

### pascal_triangle(n)

Generates Pascal's Triangle of depth `n`.

**Parameters:**

- `n` (integer): The depth of the triangle.

**Returns:**

- List of Lists: Pascal's Triangle represented as a list of lists.

**Example:**

```python
triangle = pascal_triangle(5)
print(triangle)
```

**Output:**

```
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```

### print_triangle(n)

Prints Pascal's Triangle of depth `n`.

**Parameters:**

- `n` (integer): The depth of the triangle.

**Example:**

```python
print_triangle(5)
```

**Output:**

```
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

