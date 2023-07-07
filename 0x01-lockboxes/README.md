# 0x01-lockboxes

This repository contains a solution for the "Lockboxes" problem. The problem involves determining whether all the boxes in a given list of boxes can be opened by using keys stored in the boxes.

## Problem Description

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from 0 to `n - 1` and may contain keys to other boxes. The goal is to determine if it's possible to open all the boxes.

## Solution

The solution is provided in the `0-lockboxes.py` file. It defines a function `canUnlockAll(boxes)` that takes a list of lists `boxes` as input. Each sublist represents a box and contains keys to other boxes. The function returns `True` if all the boxes can be opened and `False` otherwise.

## Usage

To test the solution, you can run the provided `main_0.py` script. It demonstrates the usage of the `canUnlockAll` function with different input cases and prints the results.

```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
```

The expected output of running `main_0.py` is as follows:

```
True
True
False
```

## Repository

GitHub repository: [alx-interview](https://github.com/Markson17/alx-interview)

Directory: 0x01-lockboxes
File: 0-lockboxes.py

Feel free to explore the repository for the solution code and further reference.