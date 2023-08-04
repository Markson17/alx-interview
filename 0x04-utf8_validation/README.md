# 0x04UTF-8 Validation

This Python script, `0-validate_utf8.py`, implements a method that determines whether a given data set represents a valid UTF-8 encoding. It takes a list of integers as input, where each integer represents 1 byte of data (8 least significant bits). The script validates the UTF-8 encoding based on the following rules:

- A character in UTF-8 can be 1 to 4 bytes long.
- The data set can contain multiple characters.

## Getting Started

To use this script, follow these steps:

1. Clone this repository to your local machine or download the `valid_utf8.py` file.
2. Ensure you have Python 3 installed on your system.

## How to Use

In your Python script or interactive session, import the `validUTF8` function from `valid_utf8` module and call it with a list of integers as the argument. The function will return `True` if the data is a valid UTF-8 encoding, and `False` otherwise.

```python
from valid_utf8 import validUTF8

data = [65]
print(validUTF8(data))  # Output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False
```
