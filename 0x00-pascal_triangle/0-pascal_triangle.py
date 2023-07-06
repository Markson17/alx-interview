#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    if n <= 0:
        return []  # Return an empty list if n is less than or equal to 0

    triangle = [[1]]  # Initialize the triangle with the first row [1]

    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            # Calculate the value for each position in the current row by summing the corresponding elements from the previous row
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # End each row with 1
        triangle.append(row)  # Append the row to the triangle

    return triangle  # Return the Pascal's triangle as a list of lists



def print_triangle(n):
    """
    Print the Pascal's triangle
    """
    triangle = pascal_triangle(n)
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


