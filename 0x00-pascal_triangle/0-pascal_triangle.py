#!/usr/bin/python3

def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle up to n rows."""
    if n <= 0:
        return []
    
    triangle = [[1]]  # Initialize with the first row
    
    for i in range(1, n):
        row = [1]  # Every row starts with 1
        for j in range(1, i):
            # Each number is the sum of the two numbers above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Every row ends with 1
        triangle.append(row)
    
    return triangle
