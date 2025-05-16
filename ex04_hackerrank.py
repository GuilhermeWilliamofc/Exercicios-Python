"""
HackerRank - Loops

Task
The provided code stub reads an integer, , from STDIN. For all non-negative integers i < n, print i^2.

Example

The list of non-negative integers that are less than n = 3 is [0, 1, 2]. Print the square of each number on a separate line.
"""

number = int(input())

for n in range(0, number):
    print(n * n)
