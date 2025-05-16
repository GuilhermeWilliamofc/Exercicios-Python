"""
HackerRank - Python: Division

Task
The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

No rounding or formatting is necessary.
"""

first_number = float(input(""))
second_number = float(input(""))

# integer division
first_division = first_number // second_number

# float division
second_division = first_number / second_number

# prints
print(first_division)
print(second_division)
