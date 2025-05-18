"""
HackerRank - Print Function

The included code stub will read an integer, n, from STDIN.

Without using any string methods, try to print the following:
123...n
Note that "..." represents the consecutive values in between.

Example
n = 5
Print the string 12345.

Input Format

The first line contains an integer n.

Output Format

Print the list of integers from 1 through n as a string, without spaces.
"""


def print_sequence(number):
    for num in range(1, number + 1):
        print(num, end="")


try:
    n = int(input())
except ValueError:
    print("Please enter a valid number")
else:
    print_sequence(n)
