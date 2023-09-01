# 0-island_perimeter.py
This repository contains a Python script that calculates the perimeter of an island described in a grid.

## Task Description

You are provided with a grid, where:
- `0` represents water
- `1` represents land

Each cell in the grid is square and has a side length of 1. Cells are connected horizontally and vertically, but not diagonally. The grid is rectangular, with its width and height not exceeding 100. The grid is completely surrounded by water, and there is only one island or nothing at all. The island doesn’t have any "lakes" (i.e., water inside that isn't connected to the water surrounding the island).

## Function

The main function, `island_perimeter(grid)`, calculates and returns the perimeter of the island described in the input `grid`.

### Example

Consider the following input grid:
```
[
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
```
The corresponding output for this input would be `12`, as there are 12 edges that form the perimeter of the island.

## Usage

To use the script, you can import the `island_perimeter` function from the `0-island_perimeter.py` file and pass the grid as an argument to the function.

```python
from 0-island_perimeter import island_perimeter

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

perimeter = island_perimeter(grid)
print(perimeter)  # Output: 12
```

