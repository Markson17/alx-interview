# 0x08-making_change

This repository contains a Python script that implements an algorithm for solving the problem of making change using the fewest number of coins. Given a pile of coins of different values and a target amount total, the script determines the minimum number of coins required to meet the total using the available coin denominations.

## Usage

To use the `makeChange` function from the `0-making_change.py` script, follow these steps:

1. Make sure you have Python 3 installed on your system.

2. Clone the repository:

   ```
   git clone https://github.com/your-username/alx-interview.git
   ```

3. Navigate to the `0x08-making_change` directory:

   ```
   cd alx-interview/0x08-making_change
   ```

4. Open the `0-making_change.py` script in your preferred text editor to review the implementation:

   ```
   vim 0-making_change.py
   ```

5. In the script, the `makeChange` function takes two arguments:
   - `coins`: A list of coin denominations (positive integers) available for making change.
   - `total`: The target amount for which change needs to be made.

6. Run the script by executing the provided `0-main.py` file:

   ```
   python3 0-main.py
   ```

7. The script will output the fewest number of coins needed to meet the target total for each test case.

## Example

Given the following examples:

```python
print(makeChange([1, 2, 25], 37))    # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))    # Output: -1
```

- In the first example, the available coins are [1, 2, 25], and the target total is 37. The minimum number of coins needed to make 37 is 7 (25 + 2 + 2 + 2 + 2 + 2 + 2).
- In the second example, there is no combination of the given coin denominations that can add up to 1453, so the function returns -1.

