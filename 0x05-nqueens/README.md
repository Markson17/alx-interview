# N Queens

The N queens puzzle is a classic chess problem that involves placing N non-attacking queens on an N×N chessboard. The challenge is to find all possible solutions for this problem.

## Usage

To solve the N queens problem, run the program as follows:

```
nqueens N
```

Where `N` must be an integer greater than or equal to 4. The program will then print every possible solution to the N queens problem, with each solution represented as a list of coordinates indicating the positions of the queens on the chessboard.

## Constraints

- The program should only be imported with the `sys` module.
- If the user provides the wrong number of arguments, the program will print: `Usage: nqueens N` and exit with status 1.
- If `N` is not a valid integer, the program will print: `N must be a number` and exit with status 1.
- If `N` is less than 4, the program will print: `N must be at least 4` and exit with status 1.

## Example

```
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

```
$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```
