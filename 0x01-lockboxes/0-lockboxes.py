#!/usr/bin/python3
"""
This module defines a function that determines if a box containing a list
of lists can be opened using keys stored in the lists.
"""


def canUnlockAll(boxes):
    """
    Determines if boxes can be unlocked.

    Args:
        boxes (list): A list of lists representing the boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    position = 0  # Current position in the boxes
    unlocked = {}  # Dictionary to keep track of unlocked boxes

    for box_index, box in enumerate(boxes):
        if len(box) == 0 or position == 0:
            # If the box is empty or it's the first box, mark it as always unlocked
            unlocked[position] = "always_unlocked"

        for key in box:
            # Check if the key is valid and not the current box's position
            if key < len(boxes) and key != position:
                unlocked[key] = key

        if len(unlocked) == len(boxes):
            # If all boxes are unlocked, return True
            return True

        position += 1

    # If all boxes couldn't be unlocked, return False
    return False
