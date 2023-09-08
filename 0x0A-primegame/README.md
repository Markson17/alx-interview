# 0x0A-primegame

Maria and Ben are playing a game where they take turns choosing prime numbers from a set of consecutive integers. The set starts from 1 up to and including n. The objective is to remove the chosen prime number and all its multiples from the set. The player who cannot make a move loses the game.

In this game, Maria always goes first, and both players play optimally. Your task is to determine the winner of each round and find out who won the most rounds out of x rounds.

## Function Signature

```python
def isWinner(x, nums):
    """
    Determine the winner of the prime game for each round and return the player who won the most rounds.

    Args:
        x (int): The number of rounds to play.
        nums (list of int): An array of integers, where each integer 'n' represents the upper boundary of the range
                            for each round. The range starts from 1 and goes up to 'n'.

    Returns:
        str or None: The name of the player that won the most rounds (either "Maria" or "Ben"). 
                     If the winner cannot be determined, return None.

    Constraints:
    - n and x will not be larger than 10000.
    - Do not import any additional packages.
    """
```

## Example

```python
x = 3
nums = [4, 5, 1]

# First round: 4
# Maria picks 2 and removes 2, 4, leaving 1, 3
# Ben picks 3 and removes 3, leaving 1
# Ben wins because there are no prime numbers left for Maria to choose

# Second round: 5
# Maria picks 2 and removes 2, 4, leaving 1, 3, 5
# Ben picks 3 and removes 3, leaving 1, 5
# Maria picks 5 and removes 5, leaving 1
# Maria wins because there are no prime numbers left for Ben to choose

# Third round: 1
# Ben wins because there are no prime numbers for Maria to choose

# Result: Ben has the most wins

# Output:
# "Ben"
```

## Usage

```python
from prime_game import isWinner

x = 3
nums = [4, 5, 1]

winner = isWinner(x, nums)
print("Winner: {}".format(winner))
```
